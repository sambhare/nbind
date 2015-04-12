{
	"include_dirs": [
		"include"
	],
	"sources": ["src/Binding.cc"],
	"cflags": ["-std=c++11"],
	"xcode_settings": {
		"MACOSX_DEPLOYMENT_TARGET": "10.7",
		"OTHER_CPLUSPLUSFLAGS":[
			"-std=c++11",
			"-stdlib=libc++"
		],
		"OTHER_LDFLAGS": ["-stdlib=libc++"]
	}
}
