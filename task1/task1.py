import subprocess
import socket
import csv


def main():
    domains = ['google.com', 'kaggle.com', 'vk.com', 'ok.ru', 'stackoverflow.com',
               'whatsapp.com', 'anekdotov.net', 'youtube.com', 'pythontutorial.net', 'drive.ru']
    header = ['domain', 'ip address', 'avg ping']
    f = open('out.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    for domain in domains:
        cmd = ['ping', domain]
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        if result.returncode == 0:
            res = result.stdout.decode('cp866')
            ind_of_avg = res.find('Среднее = ') + len('Среднее = ')
            end_ind_avg = res.find(' ', ind_of_avg)
            avg = res[ind_of_avg:end_ind_avg]
            ip = socket.gethostbyname(domain)
            writer.writerow([domain, ip, avg])
    f.close()


if __name__ == "__main__":
    main()
