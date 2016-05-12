# autoLib
这是一个将ios静态库工程自动打包生成.a文件的脚本


# Usage

     -t -target 工程名
     
     
     cd进入静态库工程文件夹并且把autoLib.py放入其中
     
     $ python autobuild.py -t libStaticLib（工程名）
     
     
     如果执行成功
     
     ** BUILD SUCCEEDED **

     output: ~/desktop/libStaticLib.a
     
    会将生成的.a文件生成到桌面上
     