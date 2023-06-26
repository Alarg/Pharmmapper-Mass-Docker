import sys
import os
import requests
from bs4 import BeautifulSoup

def download_site(url, verbose=False):
    # Create the .temp directory if it does not exist
    if not os.path.exists('.temp'):
        os.makedirs('.temp')

    # Download the website and save it to .temp/site.html
    if verbose:
        print(f'Downloading {url}...')
    response = requests.get(url)
    with open('.temp/site.html', 'w') as f:
        f.write(response.text)

    if verbose:
        print('Site downloaded')

def parse_site(verbose=False):
    with open('.temp/site.html', 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        if verbose:
            print('Parsing site...')

        # Find all the download links for the aligned ligands
        ligand_links = soup.find_all('a', string='Download Aligned Ligand')
        for i, link in enumerate(ligand_links):
            # Extract the URL for the aligned ligand and download it
            ligand_url = 'http://www.lilab-ecust.cn' + link['href']
            ligand_filename = link['href'].split('/')[-1]
            pdb_id = ligand_filename.split('_')[0]
            response = requests.get(ligand_url)
            with open(f'.temp/ligand_{pdb_id}.mol2', 'w') as f:
                f.write(response.text)
            if verbose:
                print(f'Downloaded ligand_{pdb_id}.mol2')

            # Extract the PDB ID from the file name and download the corresponding PDB file
            pdb_id = link['href'].split('/')[4][:4]
            pdb_url = f'https://files.rcsb.org/download/{pdb_id}.pdb'
            response = requests.get(pdb_url)
            with open(f'.temp/{pdb_id}.pdb', 'w') as f:
                f.write(response.text)
            if verbose:
                print(f'Downloaded {pdb_id}.pdb')

        if verbose:
            print('Done.')

def main():
    if len(sys.argv) == 2 or len(sys.argv) == 3 and sys.argv[2] == '-v':
        url = sys.argv[1]
        verbose = False
        if len(sys.argv) == 3:
            verbose = True
        download_site(url, verbose)
        parse_site(verbose)
    else:
        print('Usage: python site_parser.py url [-v]')

if __name__ == '__main__':
    main()
