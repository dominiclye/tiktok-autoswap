
import os , pycurl , datetime
from colorama import Fore, Style
from discord_webhook import DiscordEmbed, DiscordWebhook
from time import sleep
from requests import post
from getkey import getkey, key
from random import randint



def title():
    # Colour and StyleVariables
    red = Fore.RED
    cyan = Fore.CYAN
    green = Fore.GREEN
    yellow = Fore.YELLOW
    bright = Style.BRIGHT
    magenta = Fore.MAGENTA
    reset = Fore.RESET
    stylereset = Style.RESET_ALL

    # Swapper Title
    os.system('Clear')

    titleLuna = f"""{yellow}{bright}
    o                     __...__     *                         
                *   .--'    __.=-.             o             ___       __   __   __    _   _______
        |          ./     .-'                               |   |     |  | |  | |  |  | | |   _   |
        -O-        /      /                                 |   |     |  | |  | |   |_| | |  |_|  |
        |        /    '"/               *                   |   |     |  | |  | |       | |       |
                |     (@)                                   |   |___  |  |_|  | |  _    | |       |
                |        \                         .        |       | |       | | | |   | |   _   |
                |         \                                 |_______| |_______| |_|  |__| |__| |__|
    *          |       ___\                  |               
                |  .   /  `                 -O-                {reset}{magenta}The moon is beautiful, isn't it?{reset}{yellow}   
                \  `~~\                     |
            o     \     \            *         
                    `\    `-.__           .  
        .             `--._    `--'
                        `---~~`                *
                *                   o{reset}{stylereset}
    """

    for char in titleLuna:
        sleep(0.001)
        print(char, end='', flush=True)


class HTTP:
    def request(self, url, headers, data):
        return post(url=url, headers=headers, data=data).text

class Swapper:
    def __init__(self):
        self.claimed = False
        self.released = False
        self.confirmed = False
        self.attempts = 0
        self.HTTP = HTTP()

    def target(self):
        self.target = input(f'[{Fore.MAGENTA}+{Fore.RESET}] Target: ')

    def confirm_release(self):
        global releaseSID
        global claimSID
        print(f'[{Fore.MAGENTA}+{Fore.RESET}] Ready to swap {Fore.MAGENTA}@{self.target}{Fore.RESET}, press {Fore.MAGENTA}ENTER{Fore.RESET} to confirm or {Fore.MAGENTA}ESC{Fore.RESET} to exit')
        key_pressed = getkey()

        if key_pressed == key.ENTER:
            print(f"{Fore.GREEN}Starting Swap...{Fore.RESET}")
            self.confirmed = True
        elif key_pressed == key.ESCAPE:
            print(f"{Fore.RED} Exiting Swap...{Fore.RESET}")
            exit(0)

    def check_release_sid(self, releaseSID):
        self.rr = self.HTTP.request("https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?version_code=1.0.0&language=en&app_name=musical_ly&aid=1233&device_platform=iphone&request_tag_from=h5&os_api=25&device_type=G011A&ssmix=a&manifest_version_code=250709&dpi=300&region=US&carrier_region=SA&app_name=musically_go&version_name=25.7.9&timezone_offset=-21600&ts=1656128529&ab_version=25.7.9&ac2=wifi&ac=wifi&app_type=normal&channel=googleplay&update_version_code=250709&_rticket=1656128903213&device_platform=android&iid=7112982178154497798&build_number=25.7.9&locale=en&op_region=SA&version_code=250709&timezone_name=America%2FChicago&cdid=4f56d003-0871-4fe1-8df1-ec1d221e56e3&openudid=ffd5bb8e85a7c424&device_id=7109028255408014874&sys_region=US&app_language=en&resolution=900*1600&device_brand=google&language=en&os_version=7.1.2&aid=1340", {
                                    'Host': 'api16-normal-c-alisg.tiktokv.com', 'Cookie': f'sessionid={releaseSID}', 'User-Agent': 'com.zhiliaoapp.musically.go/250709 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H;tt-ok/3.12.13.2-rc.4)', 'X-Gorgon': '0'}, f'unique_id=ss')
        if '"status_code": 2091' in self.rr:
            print(
                f'[{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}RELEASE SESSION{Fore.RESET} loaded successfully.')
        elif '"status_code": 2070' in self.rr:
            print(
                f'[{Fore.YELLOW}?{Fore.RESET}] {Fore.YELLOW}RELEASE SESSION{Fore.RESET} not user-changeable.')
            exit(0)
        elif '"status_code": 8' in self.rr:
            print(
                f'[{Fore.RED}!{Fore.RESET}] {Fore.RED}RELEASE SESSION{Fore.RESET} login failed')
            exit(0)
        else:
            print()

    def check_claim_sid(self, claimSID):
        self.r = self.HTTP.request("https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?version_code=1.0.0&language=en&app_name=musical_ly&aid=1233&device_platform=iphone&request_tag_from=h5&os_api=25&device_type=G011A&ssmix=a&manifest_version_code=250709&dpi=300&region=US&carrier_region=SA&app_name=musically_go&version_name=25.7.9&timezone_offset=-21600&ts=1656128529&ab_version=25.7.9&ac2=wifi&ac=wifi&app_type=normal&channel=googleplay&update_version_code=250709&_rticket=1656128903213&device_platform=android&iid=7112982178154497798&build_number=25.7.9&locale=en&op_region=SA&version_code=250709&timezone_name=America%2FChicago&cdid=4f56d003-0871-4fe1-8df1-ec1d221e56e3&openudid=ffd5bb8e85a7c424&device_id=7109028255408014874&sys_region=US&app_language=en&resolution=900*1600&device_brand=google&language=en&os_version=7.1.2&aid=1340", {
                                   'Host': 'api16-normal-c-alisg.tiktokv.com', 'Cookie': f'sessionid={claimSID}', 'User-Agent': 'com.zhiliaoapp.musically.go/250709 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H;tt-ok/3.12.13.2-rc.4)', 'X-Gorgon': '0'}, f'unique_id=ss')
        if '"status_code": 2091' in self.r:
            print(
                f'[{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN}CLAIM SESSION{Fore.RESET} loaded successfully.')
        elif '"status_code": 2070' in self.r:
            print(
                f'[{Fore.YELLOW}?{Fore.RESET}] {Fore.YELLOW}CLAIM SESSION{Fore.RESET} not user-changeable, exiting.')
            exit(0)
        elif '"status_code": 8' in self.r:
            print(
                f'[{Fore.RED}!{Fore.RESET}] {Fore.RED}CLAIM SESSION{Fore.RESET} login failed, exiting.')
            exit(0)

    def release_and_claim(self):
        self.releaseuser = f''.join(f'lunaswap{randint(1, 100000)}')

        if self.confirmed == True:
            try:
                r = pycurl.Curl()
                r.setopt(pycurl.URL,'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?version_code=1.0.0&language=en&app_name=musical_ly&aid=1233&device_platform=iphone&request_tag_from=h5&os_api=25&device_type=G011A&ssmix=a&manifest_version_code=250709&dpi=300&region=US&carrier_region=SA&app_name=musically_go&version_name=25.7.9&timezone_offset=-21600&ts=1656128529&ab_version=25.7.9&ac2=wifi&ac=wifi&app_type=normal&channel=googleplay&update_version_code=250709&_rticket=1656128903213&device_platform=android&iid=7112982178154497798&build_number=25.7.9&locale=en&op_region=SA&version_code=250709&timezone_name=America%2FChicago&cdid=4f56d003-0871-4fe1-8df1-ec1d221e56e3&openudid=ffd5bb8e85a7c424&device_id=7109028255408014874&sys_region=US&app_language=en&resolution=900*1600&device_brand=google&language=en&os_version=7.1.2&aid=1340')
                r.setopt(pycurl.HTTPHEADER, ["Host: api16-normal-c-alisg.tiktokv.com",
                        f"Cookie: sessionid={releaseSID}", "User-Agent: com.zhiliaoapp.musically.go/250709 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H;tt-ok/3.12.13.2-rc.4)", 'X-Gorgon: 0'])
                r.setopt(pycurl.POST, 1)
                r.setopt(pycurl.POSTFIELDS, f'unique_id={self.releaseuser}')
                r.perform()
                self.released = True
                self.releasetime = datetime.datetime.now()
                print(f'[{Fore.GREEN}+{Fore.RESET}] Released {self.target} at {self.releasetime}')
            except:
                pass
        
        while self.released == True:
            c = pycurl.Curl()
            c.setopt(pycurl.URL, 'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/?version_code=1.0.0&language=en&app_name=musical_ly&aid=1233&device_platform=iphone&request_tag_from=h5&os_api=25&device_type=G011A&ssmix=a&manifest_version_code=250709&dpi=300&region=US&carrier_region=SA&app_name=musically_go&version_name=25.7.9&timezone_offset=-21600&ts=1656128529&ab_version=25.7.9&ac2=wifi&ac=wifi&app_type=normal&channel=googleplay&update_version_code=250709&_rticket=1656128903213&device_platform=android&iid=7112982178154497798&build_number=25.7.9&locale=en&op_region=SA&version_code=250709&timezone_name=America%2FChicago&cdid=4f56d003-0871-4fe1-8df1-ec1d221e56e3&openudid=ffd5bb8e85a7c424&device_id=7109028255408014874&sys_region=US&app_language=en&resolution=900*1600&device_brand=google&language=en&os_version=7.1.2&aid=1340')
            c.setopt(pycurl.HTTPHEADER, ["Host: api16-normal-c-alisg.tiktokv.com",
                     f"Cookie: sessionid={claimSID}", "User-Agent: com.zhiliaoapp.musically.go/250709 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H;tt-ok/3.12.13.2-rc.4)", 'X-Gorgon: 0'])
            c.setopt(pycurl.POST, 1)
            c.setopt(pycurl.POSTFIELDS, f'unique_id={self.target}')
            c.perform()
            if pycurl.HTTP_CODE == 200:
                self.claimtime = datetime.datetime.now()
                print(f'[{Fore.GREEN}+{Fore.RESET}] Claimed {self.target} at {self.claimtime}')
                self.claimed = True

                self.webhook = DiscordWebhook(url="https://discord.com/api/webhooks/997495909262823426/hP9pRBNpnvCLU56MasmGg8XJM5p1VICEruNl0shjyziHtRtsvhrHrFDM7xpdEyTsePQF")
                self.embed = DiscordEmbed(
                title="New Tiktok Swap!",
                description=f"<@617991956722745354> has claimed **@{self.target}** on tiktok!\nhttps://tiktok.com/@{self.target}\n\n*Shoot for the stars! <3*",
                colour=0xFFFF9F
                )
                self.embed.set_footer(text='t.me/shotguns')
                self.embed.add_embed_field(name="Release Time", value=f"`{self.releasetime}`")
                self.embed.add_embed_field(name="Claim Time", value=f"`{self.claimtime}`")
                self.embed.add_embed_field
                self.webhook.add_embed(self.embed)
                self.webhook.execute()



if __name__ == '__main__':

    title()

    sleep(0.5)
    a = Swapper()
    releaseSID = input(
        f'\n[{Fore.MAGENTA}+{Fore.RESET}] Enter the {Fore.MAGENTA}RELEASE{Fore.RESET} session: ')
    a.check_release_sid(releaseSID)
    claimSID = input(
        (f'[{Fore.MAGENTA}+{Fore.RESET}] Enter the {Fore.MAGENTA}CLAIM{Fore.RESET} session: '))
    a.check_claim_sid(claimSID)
    a.target()
    a.confirm_release()
    a.release_and_claim()
