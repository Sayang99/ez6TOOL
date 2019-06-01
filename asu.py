import os, sys

print ("\033[1;32mSilahkan Insert Username&Pasword ")

print ("\033[1;32mHubungi EZ 01 Kalo Tidak Tau Pasword Nya")

username = 'ekazeroone'      

password = 'ez01'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mSelesai Selamat Bersenag2", 

			sys.exit()



		else:

			print "\033[1;32mMaaf Password Anda salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Username Anda salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
