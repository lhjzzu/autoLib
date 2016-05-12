
from optparse import OptionParser
import subprocess
import requests

#CONFIGURATION:Debug/Release
CONFIGURATION = "Release"


def buildProject(target):

    process = subprocess.Popen("pwd", stdout=subprocess.PIPE)
    (stdoutdata, stderrdata) = process.communicate()
    buildDir = stdoutdata.strip() + '/build'
    print "buildDir: " + buildDir
    osLibPath = '%s/Release-iphoneos/libStaticLib.a' %(buildDir)
    simulatorLibPath = '%s/Release-iphonesimulator/libStaticLib.a' %(buildDir)
    print (osLibPath)
    print (simulatorLibPath)

    process.wait()
    buildOSCmd = 'xcodebuild -project %s.xcodeproj -target %s -sdk iphoneos -configuration %s ONLY_ACTIVE_ARCH="NO" ARCHS="armv7 armv7s arm64" VALID_ARCHS="armv7 armv7s arm64"' %(target,target,CONFIGURATION)
    process = subprocess.Popen(buildOSCmd, shell=True)
    process.wait()
    buildSimulatorCmd = 'xcodebuild -project %s.xcodeproj -target %s -sdk iphonesimulator -configuration %s ONLY_ACTIVE_ARCH="NO"' %(target,target,CONFIGURATION)
    process = subprocess.Popen(buildSimulatorCmd, shell=True)
    process.wait()
    output = '~/desktop/lib%s.a' %(target)
    buildLibCmd = 'lipo -create %s %s -o %s' %(osLibPath,simulatorLibPath,output)
    process = subprocess.Popen(buildLibCmd, shell=True)
    process.wait()
    print "output: " + output


def xcbuild(options):
	target = options.target

	if target is None:
		pass
	elif target is not None:
		buildProject(target)

def main():
	
	parser = OptionParser()
	parser.add_option("-t", "--target", help="Build the target specified by targetname. Required if building a project.", metavar="targetname")

	(options, args) = parser.parse_args()

	print "options: %s, args: %s" % (options, args)

	xcbuild(options)

if __name__ == '__main__':
	main()