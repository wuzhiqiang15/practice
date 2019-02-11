from redirectsplit import RedirectSplit

url = "meiyou:///ebweb?params=eyJ1cmwiOiJodHRwczovL3Rlc3QteW91bmdtYWxsLWFwaS55b3V6aWJ1eS5jb20vY2FzaE91dD9oNV92PTIuMS41Jm15d3RiX25hbWU9c2hlZXAifQ=="

s2 = RedirectSplit(url).redirect_split()

print(s2)