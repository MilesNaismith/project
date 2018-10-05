import auchan_parcer
import metro_parser
import perekrestok_parser
import db_from_csv
def main():
    auchan_parcer.main()
    metro_parser.main()
    perekrestok_parser.main()
    db_from_csv.main()

if __name__ == "__main__":   
    main()        