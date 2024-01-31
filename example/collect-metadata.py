'''
@ author: Amal Joseph Varghese
@ email: amaljova@gmail.com
@ github: https://github.com/amaljova
@ date: 13 June 2023
'''
import QuickDicom as qd
import pandas as pd
import json

def makeDataBse(item):
    # print(item)
    name = item[0]
    path = item[1]

    # print(f"Started: {path}")
    qd.logging.logger.info(f"Started: {path}")
    history = pd.DataFrame([], columns=["FilePath"])
    out_json_file = f"{name}_metadata.json"
    history_file = f"{name}_history.csv"

    try:
        qd.logging.logger.info(f"Trying to load FilePaths history from {history_file} ...")
        history = pd.read_csv(history_file)
        qd.logging.logger.info(f"FilePaths history loaded from {history_file}")
    except:
        pass
    
    data_list = qd.metadata.getData(path, history["FilePath"])
    # print(f"Finished: {path}")
    qd.logging.logger.info(f"Finished: {path}")

    #Append History
    qd.logging.logger.info(f"Updating History {history_file}")
    history = pd.concat([history,pd.DataFrame([item.get("FilePath") for item in data_list], columns=["FilePath"])])

    try:
        qd.logging.logger.info(f"Loading & Appending {out_json_file}")
        with open(out_json_file, "r") as f:
            data_list += json.load(f)
    except:
        pass

    qd.logging.logger.info(f"Writing {out_json_file} ...")
    with open(out_json_file , 'w') as f:
        json.dump(data_list, f)
        qd.logging.logger.info(f"Written {out_json_file}.")

    qd.logging.logger.info(f"Writing {history_file} ...")
    history.to_csv(history_file, index = False)
    
    # data = pd.DataFrame(data_list)
    # data.to_csv(f"{name}_metadata.csv", index=False)
    # print('CSV_file --done!')
# =========================================FIXME Block=======================================


if __name__ == '__main__':

    makeDataBse(("prefix", "/path/to/DICOM/directoy"))
    qd.logging.logger.info('All Done!')

