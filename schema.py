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
    data: List[List[object]]  # Adjust based on the specific nested structure

def generate_csv(data: List[PenData], filename: str) -> None:
    """Generate a CSV file from a list of PenData dictionaries."""
    if not data or not isinstance(data[0], dict):
        print("Invalid data format: expected a list of dictionaries.")
        return

    # Get the headers from the first dictionary
    headers = data[0].keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  
        writer.writerows(data)  

    print(f"CSV file '{filename}' generated successfully.")
