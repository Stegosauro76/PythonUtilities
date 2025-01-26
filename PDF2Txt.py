import fitz  # PyMuPDF

def estrai_testo_da_pdf(pdf_path, output_file):
    testo_completo = ''
    
    # Apri il PDF
    doc = fitz.open(pdf_path)
    
    # Estrai testo da ogni pagina
    for pagina in doc:
        testo_completo += pagina.get_text() + '\n'
    
    # Salva il testo estratto in un file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(testo_completo)

# Specifica il percorso del tuo file PDF e il nome del file di output
pdf_path = 'FS-Rules_2025_v1.1.pdf'  # Assicurati che il file abbia l'estensione .pdf
output_file = 'testo_estratto.txt'   # Nome del file di output
estrai_testo_da_pdf(pdf_path, output_file)

print(f'Testo estratto salvato in {output_file}')
