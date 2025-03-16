import etl_classes

file_input_path = 'pracownicy.csv'
file_output_path = '/home/alexzakr/programing/uam_dataeng/pracownicy.json'

def main():

    json_loader = etl_classes.JsonLoader(
        orient="records",
        index=False,
        lines=True)

    etl_job = etl_classes.Job(
        input_path=file_input_path,
        output_path=file_output_path,
        json_loader=json_loader
    )

    etl_job.run()

if __name__ == "__main__":
    main()