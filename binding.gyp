{
  "targets": [
    {
      "sources": [
        "src/addon.cpp",
        "src/argument.cpp",
        "src/argument.h",
        "src/payload.cpp",
        "src/payload.h",
        "src/capture.cpp",
        "src/capture.h",
        "src/channel.cpp",
        "src/channel.h",
        "src/client.cpp",
        "src/client.h",
        "src/clientlib.cpp",
        "src/clientlib.h",
        "src/connection.cpp",
        "src/connection.h",
        "src/error.cpp",
        "src/error.h",
        "src/event.cpp",
        "src/event.h",
        "src/filetransfer.cpp",
        "src/filetransfer.h",
        "src/helper.cpp",
        "src/helper.h",
        "src/identity.cpp",
        "src/identity.h",
        "src/log.cpp",
        "src/log.h",
        "src/playback.cpp",
        "src/playback.h",
        "src/server.cpp",
        "src/server.h",
        "src/shared.cpp",
        "src/shared.h",
      ],
      "include_dirs": [
        "includes",
        "<!(node -e \"require('nan')\")",
      ],
      "conditions": [
        ["OS==\"win\" and target_arch==\"x64\"", {
          "target_name": "ts3client_win64",
          "libraries": [
            "<(module_root_dir)/bin/win64/ts3client.lib",
          ],
          "postbuilds": [{
            "postbuild_name": "Deploy Node.js addon",
            "action": [
              "copy",
              "<@(PRODUCT_DIR)/ts3client_win64.node",
              "<(module_root_dir)/bin/win64/ts3client.node"
            ],
          }]
        }],
        ["OS==\"win\" and target_arch!=\"x64\"", {
          "target_name": "ts3client_win32",
          "libraries": [
            "<(module_root_dir)/bin/win32/ts3client.lib",
          ],
          "postbuilds": [{
            "postbuild_name": "Deploy Node.js addon",
            "action": [
              "copy",
              "<@(PRODUCT_DIR)/ts3client_win32.node",
              "<(module_root_dir)/bin/win32/ts3client.node"
            ],
          }]
        }],
        ["OS==\"linux\" and target_arch==\"x64\"", {
          "target_name": "ts3client_linux_amd64",
          "libraries": [
            "<(module_root_dir)/bin/linux_amd64/libts3client.so",
          ],
          "postbuilds": [{
            "postbuild_name": "Deploy Node.js addon",
            "action": [
              "cp",
              "<@(PRODUCT_DIR)/ts3client_linux_amd64.node",
              "<(module_root_dir)/bin/linux_amd64/ts3client.node"
            ],
          }]
        }],
        ["OS==\"linux\" and target_arch!=\"x64\"", {
          "target_name": "ts3client_linux_x86",
          "libraries": [
            "<(module_root_dir)/bin/linux_x86/libts3client.so",
          ],
          "postbuilds": [{
            "postbuild_name": "Deploy Node.js addon",
            "action": [
              "cp",
              "<@(PRODUCT_DIR)/ts3client_linux_x86.node",
              "<(module_root_dir)/bin/linux_x86/ts3client.node"
            ],
          }]
        }],
        ["OS==\"mac\"", {
          "target_name": "ts3client_darwin",
          "libraries": [
            "<(module_root_dir)/bin/darwin/libts3client.dylib",
          ],
          "postbuilds": [{
            "postbuild_name": "Adjust link path to TeamSpeak SDK ClientLib",
            "action": [
              "install_name_tool",
              "-change",
              "/usr/local/lib/libts3client.dylib",
              "@loader_path/libts3client.dylib",
              "<@(PRODUCT_DIR)/ts3client.node"
            ],
          },
          {
            "postbuild_name": "Deploy Node.js addon",
            "action": [
              "cp",
              "<@(PRODUCT_DIR)/ts3client_darwin.node",
              "<(module_root_dir)/bin/darwin/ts3client.node"
            ],
          }]
        }],
      ]
    }
  ]
}
