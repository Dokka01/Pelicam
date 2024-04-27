





<!-- Ctrl + Shift + V pour avoir le preview du readme -->








<!-- PROJECT LOGO -->

<br />
<div align="center">
    <img src="data/pelicon.jpeg" alt="Logo" width="120" height="auto">
    <h1>Pelicam</h1>
    <p>BOUDES Clément et SOURGET Grégoire</p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Pelicam is an open-source project developed to improve local network security by identifying and raising awareness of IP camera vulnerabilities. It is designed for security researchers, cybersecurity professionals and technology enthusiasts who want to understand and mitigate the risks associated with these connected devices. Our aim is for the project to be continually updated and improved. Our tool can be used as a simple scanner of cameras on a network, or as an attack tool to capture video streams or even change camera settings. 


### Built With
* [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
* [Scapy](https://scapy.readthedocs.io/en/latest/)
* [PyPi](https://pypi.org/)
* [Nmap](https://nmap.org/)
* [Wireshark](https://www.wireshark.org/)
* [psutil](https://psutil.readthedocs.io/en/latest/)
* [Onvif](https://www.onvif.org/)

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites


* Need python and an IDE

* Install this library list :
    * ` scapy==2.5`
    * ` opencv-python==4.9`
    * ` onvif_zeep==0.2`
    * ` psutil==5.9.8`

    

### Installation

Here's how to use Pelicam

1. Run `main.py`

2. Check if all the libraries are installed. 
   You can verify this by running the following command in your terminal : 
   ```sh
   pip freeze
   ```
3. If the folder is complete, it should look like this :
    ```
    Pelicam/
    └── data
        ├── credentials.json
        ├── manuf.txt
        └── pelicam.jpg
    └── results
        ├── Screenshots
        ├── Onvif Links.txt
        └── RTSP Links.jpg
    ├── attack_onvif.py
    ├── attack_rtsp.py
    ├── main.py
    ├── README.md
    └── scanner.py
    ```




<!-- USAGE EXAMPLES -->
## Usage

Here's an example of how to use Pelicam. [Yotube_video](https://www.youtube.com/watch?v=DiBDtxv5pno)

<!-- ROADMAP -->
## Roadmap

- [x] info of the cam OpenCV
- [ ] instore github in our project
- [ ] more cam options with Onvif
- [ ] GUI with PyQt
- [ ] convert the file into a linux /windows app
- [ ] be able to manage several cam
- [ ] Facial recognition with AI
- ....










