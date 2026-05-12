import re

files = [
    "docs/assets/zh-CN/visual-spec-workflow.svg",
    "docs/assets/en-US/visual-spec-workflow.svg",
    "docs/assets/ja-JP/visual-spec-workflow.svg"
]

def update_svg(content):
    # 1. Update Canvas height
    content = re.sub(r'height="1180" viewBox="0 0 1400 1180"', r'height="1280" viewBox="0 0 1400 1280"', content)
    content = re.sub(r'<rect class="bg" x="0" y="0" width="1400" height="1180"/>', r'<rect class="bg" x="0" y="0" width="1400" height="1280"/>', content)
    
    # 2. Update Lane height
    content = re.sub(r'height="1060"', r'height="1160"', content)
    
    def repl(m):
        prefix = m.group(1)
        y = int(m.group(2))
        suffix = m.group(3)
        
        offset = 0
        if 710 <= y <= 788:
            offset = 10
        elif 790 <= y <= 867:
            offset = 30
        elif 870 <= y <= 947:
            offset = 50
        elif 950 <= y <= 1027:
            offset = 70
        elif 1030 <= y <= 1108:
            offset = 90
            
        return f"{prefix}{y + offset}{suffix}"
    
    # Replace y attributes in rect, text
    content = re.sub(r'(<rect class="box" x="\d+" y=")(\d+)(")', repl, content)
    content = re.sub(r'(<text class="(?:boxTitle|boxText|path)" x="\d+" y=")(\d+)(")', repl, content)
    
    # Replace middle arrows
    content = content.replace('d="M 680 690 C 680 700, 680 702, 680 710"', 'd="M 680 690 C 680 705, 680 710, 680 720"')
    content = content.replace('d="M 680 780 C 680 785, 680 787, 680 790"', 'd="M 680 790 C 680 805, 680 810, 680 820"')
    content = content.replace('d="M 680 860 C 680 865, 680 867, 680 870"', 'd="M 680 890 C 680 905, 680 910, 680 920"')
    content = content.replace('d="M 680 940 C 680 945, 680 947, 680 950"', 'd="M 680 990 C 680 1005, 680 1010, 680 1020"')
    content = content.replace('d="M 680 1020 C 680 1025, 680 1027, 680 1030"', 'd="M 680 1090 C 680 1105, 680 1110, 680 1120"')
    
    # Replace right arrows
    content = content.replace('d="M 870 745 C 905 745, 920 745, 945 745"', 'd="M 870 755 C 905 755, 920 755, 945 755"')
    content = content.replace('d="M 870 825 C 905 825, 920 825, 945 825"', 'd="M 870 855 C 905 855, 920 855, 945 855"')
    content = content.replace('d="M 870 905 C 905 905, 920 905, 945 905"', 'd="M 870 955 C 905 955, 920 955, 945 955"')
    content = content.replace('d="M 870 985 C 905 985, 920 985, 945 985"', 'd="M 870 1055 C 905 1055, 920 1055, 945 1055"')
    content = content.replace('d="M 870 1065 C 905 1065, 920 1065, 945 1065"', 'd="M 870 1155 C 905 1155, 920 1155, 945 1155"')
    
    return content

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = update_svg(content)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file}")
