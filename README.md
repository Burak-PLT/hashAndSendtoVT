# hashAndSendtoVT
This Python script hashes a file on your Windows system and sends it to VirusTotal using API v2.
You need to replace the part <YOUR_API_KEY_HERE> with the API key you have (sign up to VirusTotal). You need Python 3+ on your system.
You can Shift+RightClick on any file on your PC and choose 'Copy As Path', then put the path into the script to run it against the VirusTotal's database!

NOTE: If a hash comes back clean from VirusTotal, it doesn't necessarily mean the file is safe. By changing arbitrary data in the file, the hash of the file can be
changed drastically. Therefore, for more accurate results, try uploading the file to VirusTotal.
