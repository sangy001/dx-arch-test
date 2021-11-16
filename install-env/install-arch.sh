set -x

ARCH_VERSION="1.2.0-703"
MASTER_NAME="dce-10-6-128-50"
WORKER_NAME1="dce-10-6-128-51"
WORKER_NAME2="dce-10-6-128-52"
DCE_REGISTRY="10.6.128.169"

function login
{
    /usr/bin/expect <<EOF
	    set timeout 600
        spawn su root
	    puts "下载安装包"
	    expect "]#"
	    send "sftp 10.6.128.6\r"
	    expect "password:"
      send "dangerous\r"
      expect "sftp>"
      send "get dx-arch-${ARCH_VERSION}.tar.gz\r"
      expect "sftp>"
      send "quit\r"
	    expect "]#"
		puts "解压压缩包dx-arch-${ARCH_VERSION}.tar.gz"
		send "tar xvzf dx-arch-${ARCH_VERSION}.tar.gz\r"
	  	expect "]#"
        send "docker login ${DCE_REGISTRY}\r"
        expect {
			"Username:" {
			 	send "admin\r"
                expect "Password:"
                send "changeme\r"
			}
			"]#" {
				puts "可进入安装目录"
				send "\r"
			}
		}
		expect "]#"
		puts "进入目录dx-arch-package-${ARCH_VERSION}"
		send "cd dx-arch-package-${ARCH_VERSION}\r"
		expect "]#"
		puts "开始安装"
		send "ls\r"
        send "./install.sh \r"
	    expect "daocloud.io/daocloud]:"
	    send "${DCE_REGISTRY}/dx-arch\r"
		expect "y/n]:"
		send "y \n"
		expect "dx-arch]:"
	    send "\r"
	    expect "y/n]:"
	    send "y\r"
		expect "y/n]:"
	    send "y\r"
		expect "First Local PV Data Node Name:"
	    send "${MASTER_NAME}\r"
	    expect "Second Local PV Data Node Name:"
	    send "${WORKER_NAME1}\r"
	    expect "y/n]:"
	    send "y\r"
	    expect "Please Enter the Node Name to save the pg backup files on:"
	    send "${WORKER_NAME2}\r"
	    expect "y/n]:"
	    send "y\r"
		expect "y/n, default: n]:"
		send "n\r"
		expect "username/password: admin/changeme"
		puts "安装成功"
		send  "\n"
        expect "]#"
EOF
	return 0
}


login
if [ $? == 0 ]
then
    echo "$?"
    exit 0
fi

echo "安装成功"