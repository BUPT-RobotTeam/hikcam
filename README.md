# HIKCAM
## 概述
跨平台的海康工业摄像头 Python 驱动层，使用 C++ 实现。可高速（>60Hz）、低延迟（<5ms）获取图像数据，并使用 `OpenCV` 等来处理图像。

默认仅支持1280x1024分辨率。其他分辨率需要修改`hikcam.cpp`

## 依赖
- OpenCV
- pybind11
- Python3
- 机器视觉工业相机客户端MVS
- 机器视觉工业相机SDK Runtime组件包

## 构建: Linux
```sh
mkdir build
cd build
cmake ..
make
```
- 可能需要另行配置库的查找路径，例如修改 CMakeLists.txt：
```cmake
find_package(OpenCV REQUIRED PATHS /usr/lib/aarch64-linux-gnu/cmake/opencv4)
find_package(pybind11 REQUIRED PATHS /usr/lib/cmake/pybind11)
```

## 构建: Windows
1. 使用 CMake 生成构建目录（需要 vcpkg 的工具链文件）
```ps
mkdir build
cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE="[path to vcpkg]/scripts/buildsystems/vcpkg.cmake"
```

> 注意输出信息中`-- Found Python3: .../python3/python.exe`可能和全局环境中的版本不一致，导致后面 python import 报错。使用与库相同版本的Python即可。

1. Visual Studio 生成工具使用 Release 配置构建 pyd 库
> 默认的 Debug 配置可能由于未安装 Debug 版的Python库而报错
- 打开开发人员PowerShell
```ps
msbuild hikcam.sln /property:Configuration="Release"
```
- 也可以使用 Visual Studio IDE 打开 hikcam.sln 手动构建

- 在生成目录下找到 `hikcam.cp310-win_amd64.pyd`（依环境可能文件名不同）

2. 复制必要的dll  
- 将 `C:\Program Files (x86)\Common Files\MVS\Runtime\Win64_x64` 目录下的 dll 文件复制到 pyd 文件目录下。

## 运行 Demo
```sh
python ./capture.py
```
