## 🧩 SymbiMC: Automated Verilog Verification with Modelchecker

**SymbiMC** is a streamlined formal verification framework that combines the [SymbiYosys (SBY)](https://github.com/YosysHQ/sby) frontend with the high-performance [Modelchecker](https://github.com/ISCAS-modelchecker/modelchecker) backend. It enables automatic translation of Verilog source directories into ready-to-run `.sby` jobs, supporting rapid bit-level model checking of real-world designs like those from [XiangShan](https://github.com/OpenXiangShan/XiangShan).

<!-- **SymbiMC** is a streamlined formal verification framework built atop [SymbiYosys (SBY)](https://github.com/YosysHQ/sby) and powered by the [Modelchecker](https://github.com/ISCAS-modelchecker/modelchecker) engine. It automatically constructs `.sby` configuration files from a folder of Verilog modules, enabling fast, scalable, and fully automated bit-level property checking—especially suited for complex SoC designs such as those in [XiangShan](https://github.com/OpenXiangShan/XiangShan). -->

<!-- **[Modelchecker](https://github.com/ISCAS-modelchecker/modelchecker)** can serve as a backend solver in the [SymbiYosys (SBY)](https://github.com/YosysHQ/sby) formal verification flow, enabling fast bit-level checking of Verilog designs, such as modules from [XiangShan](https://github.com/OpenXiangShan/XiangShan). -->

### ✅ One-Command Verification Flow

```bash
# 1. Load OSS-CAD Suite environment (adjust path as needed)
source /path/to/oss-cad-suite/environment

# 2. Generate an .sby script from a folder of Verilog files
python3 gen_sby.py /path/to/verilog_folder

# 3. Run SymbiYosys with Modelchecker
cd /path/to/verilog_folder
python3 /path/to/SymbiMC/sbysrc/sby.py ./auto_gen.sby -f --modelchecker /path/to/modelchecker
```

This will: 

- Auto-detect all `.v/.sv` files in the folder

- Generate a complete `.sby` job targeting the specified `--top` module (default: `VerifyTop`)

- Launch formal verification using Modelchecker as the AIG engine backend

By default, `gen_sby.py` will:

- Use `VerifyTop` as the default top module if `--top` is not specified

- Write the output `.sby` script as `auto_gen.sby` in the same folder if --output is not provided

You can override these with:

```bash
python3 gen_sby.py /path/to/verilog_folder --top MyTopModule --output my_verify.sby
```

<!--### 📦 Example: Verifying a XiangShan Module
```bash
# Load OSS-CAD Suite environment (adjust the path accordingly)
source /path/to/oss-cad-suite/environment

# Navigate to the target test directory
cd ./sby/benchmark/CoupledL2/CoupledL2_L2AsL1_TileLink_mshrCtl_0508_2L2_L3

# Run SymbiYosys with Modelchecker as the backend solver
python3 ./sby/sbysrc/sby.py ./sby/benchmark/CoupledL2/verify_aig.sby -f --modelchecker ./sby/modelchecker
```
⚠️ Make sure to adjust `/path/to/oss-cad-suite/` to your actual OSS-CAD Suite location. -->

### ⚙️ Optional: Improve Trace Replay Speed
To accelerate trace replay during bug discovery, switch from `yices` to `bitwuzla` in SBY’s BMC mode script:

```python
# File: sbysrc/sby_mode_bmc.py
# Before (line 23):
task.handle_str_option("aigsmt", "yices")
# After:
task.handle_str_option("aigsmt", "bitwuzla")
```

### 🔗 Resources

- 📚 [SymbiYosys Documentation](https://yosyshq.readthedocs.io/projects/sby/)
- 💾 [OSS CAD Suite (Free Download)](https://github.com/YosysHQ/oss-cad-suite-build/releases)
- 🧪 [Tabby CAD Suite (Evaluation License)](https://www.yosyshq.com/tabby-cad-datasheet)