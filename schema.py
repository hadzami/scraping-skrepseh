from typing import TypedDict, List, Optional
import csv

class PenData(TypedDict):
    penId: str
    penNoDDC: Optional[str]
    penEntriUtama: str
    penJudul: str
    penDeskripsiFisik: Optional[str]
    penCatatanUmum: Optional[str]
    penKataKunci: str
    penEntriTambahan: str
    penBhsId: str
    penJnspenId: str
    penKota: str
    penTahun: str
    penPenerbit: str
    penAbstraksi: str
    penAbstract: str
    tglEdit: Optional[str]
    userEdit: Optional[str]
    penTerimaId: str
    penDigitasiId: Optional[str]
    penIjinPublikasiId: Optional[str]
    penPathCover: Optional[str]
    penCatatanBibliografi: Optional[str]
    penEntriTambahanKonprensi: Optional[str]
    penEntriTambahanOrang: Optional[str]
    penHalPendahuluan: Optional[str]
    penProdi: Optional[str]
    penProdiMigrasi: str
    penAllowFulltext: str
    penTglTambah: Optional[str]
    penUserIdTambah: Optional[str]
    penTglUbah: Optional[str]
    penUserIdUbah: Optional[str]
    penNoKlasifikasi: Optional[str]
    penTglTambah_etd2017: Optional[str]
    penUserIdTambah_etd2017: Optional[str]
    penTglUbah_etd2017: Optional[str]
    penUserIdUbah_etd2017: Optional[str]
    pbtId: str
    pbtName: str
    pbtKota: str
    jnspenId: str
    jnspenJenisPenelitian: str
    prodiId: str
    prodiFakKode: str
    prodiNama: str

class ApiResponse(TypedDict):
    draw: str
    recordsFiltered: int
    recordsTotal: int
    data: List[List[PenData]]  # Adjust based on the specific nested structure

def generate_csv(data: List[List[PenData]], filename: str) -> None:
    # Define field names explicitly
    fieldnames = [
        'penId', 'penNoDDC', 'penEntriUtama', 'penJudul',
        'penDeskripsiFisik', 'penCatatanUmum', 'penKataKunci',
        'penEntriTambahan', 'penBhsId', 'penJnspenId',
        'penKota', 'penTahun', 'penPenerbit', 'penAbstraksi',
        'penAbstract', 'tglEdit', 'userEdit', 'penTerimaId',
        'penDigitasiId', 'penIjinPublikasiId', 'penPathCover',
        'penCatatanBibliografi', 'penEntriTambahanKonprensi',
        'penEntriTambahanOrang', 'penHalPendahuluan', 'penProdi',
        'penProdiMigrasi', 'penAllowFulltext', 'penTglTambah',
        'penUserIdTambah', 'penTglUbah', 'penUserIdUbah',
        'penNoKlasifikasi', 'penTglTambah_etd2017',
        'penUserIdTambah_etd2017', 'penTglUbah_etd2017',
        'penUserIdUbah_etd2017', 'pbtId', 'pbtName', 'pbtKota',
        'jnspenId', 'jnspenJenisPenelitian', 'prodiId',
        'prodiFakKode', 'prodiNama'
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in data:
            if isinstance(item[1], dict):  # Ensure item is a dictionary
                writer.writerow(item[1])
            else:
                print("Item is not a dictionary:", item)

    print(f"CSV file '{filename}' generated successfully.")
