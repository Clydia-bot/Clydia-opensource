# Clydia-opensource
## 🤓 Auto Hébergement

> Les étapes montrées dans ce tutoriel ont été faites avec Ubuntu 18.04

### 🖥 Voici les OS qui marchent avec Clydia :

|            OS             | Testé | Marche |
| :-----------------------: | :---: | :----: |
| Ubuntu (16.04, 18.04, 20) |  ✅   |   ✅   |
|          Fedora           |  ❌   |   ✅   |
|        Windows 10         |  ❌   |   ✅   |
|         Windows 7         |  ❌   |   ✅   |
|           MacOS           |  ✅   |   ✅   |
|         Raspberry         |  ✅   |   ✅   |

### 🖥 Configuration système :

Clydia est basé sur Discord.Py, qui consomme très peu de ressources. Clydia demande au minimum 500Mo de RAM. Si vous souhaitez faire tourner Clydia sur plusieurs serveurs, nous vous conseillons 1Go de RAM.

### 🤓 Configuration de Clydia :

Pour configurer Clydia, suivez les étapes ci dessous :

1.  Générer un token de bot via l'interface Discord Developer.
2.  Rentrez les commandes suivantes dans un terminal sur votre machine

```
apt update
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
sudo apt install python3-pip
sudo apt install git
git clone https://github.com/Clydia-bot/Clydia-opensource.git
cd Clydia-opensource
python3 -m pip install -U discord.py
```

3.  Allez dans le fichier main.py puis chercher la ligne `client.run('TOKENHERE`) puis rentrez ici votre token Discord
4.  tapez la commande `python3 main.py`
5.  Voilà Clydia est prêt 🍾
