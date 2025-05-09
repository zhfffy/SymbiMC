#!/usr/bin/env python3
# python3 gen_sby.py /path/to/verilog_folder --top MyTopModule --output my_verify.sby

import os
import argparse

def generate_full_sby_script(directory, top_module="VerifyTop", output_file="auto_gen.sby"):
    # 获取所有 .v 和 .sv 文件
    verilog_files = [
        f for f in os.listdir(directory)
        if f.endswith(".v") or f.endswith(".sv")
    ]
    verilog_files.sort()

    if not verilog_files:
        print("[!] No Verilog files found in the specified directory.")
        return

    # 构造 .sby 内容
    options = "[options]\nmode bmc\ndepth 2000\nvcd on\n\n"
    engines = "[engines]\naiger modelchecker\n\n"
    
    script = "[script]\nread_verilog -sv " + " ".join(verilog_files) + "\n"
    script += f"prep -top {top_module} -nordff\n\n"

    files = "[files]\n" + "\n".join(verilog_files) + "\n"

    sby_content = options + engines + script + files

    # 写入 .sby 文件
    output_path = os.path.join(directory, output_file)
    with open(output_path, "w") as f:
        f.write(sby_content)

    print(f"[✔] Generated: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto-generate a .sby script for SymbiMC.")
    parser.add_argument("directory", help="Path to folder containing Verilog files")
    parser.add_argument("--top", default="VerifyTop", help="Top module name (default: VerifyTop)")
    parser.add_argument("--output", default="auto_gen.sby", help="Output .sby filename (default: auto_gen.sby)")

    args = parser.parse_args()
    generate_full_sby_script(args.directory, args.top, args.output)