import argparse
import os
import xml.dom.minidom

if __name__ == '__main__':

    # 검색할 경로를 option 으로 전달받음

    parser = argparse.ArgumentParser(description='xml formatter')
    parser.add_argument('--path', type=str, help='Path to search xml files')
    args = parser.parse_args()

    # 전달받은 경로가 없으면 현재 경로를 사용
    if args.path:
        FULL_PATH = args.path
    else:
        FULL_PATH = os.getcwd()

    # 경로의 모든 xml파일 조회
    for file in os.listdir(FULL_PATH):
        if file.endswith('.xml'):
            full_file_path = os.path.join(FULL_PATH, file)
            print("Formatting", full_file_path)

            # xml 파일을 읽어서 formatted xml로 그대로 저장
            formatted_xml = ''
            with open(full_file_path, 'r') as f:
                xml_str = f.read()
                dom = xml.dom.minidom.parseString(xml_str)
                formatted_xml = dom.toprettyxml()

            with open(full_file_path, 'w') as f:
                f.write(formatted_xml)

