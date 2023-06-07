#Le fichier créé doit être ici: /usr/share/backgrounds/contest/
'''
Le fichier de configuration doit-être ici: /usr/share/gnome-background-properties/
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<wallpapers>
 <wallpaper deleted="false">
   <name>Wood</name>
   <filename>/usr/share/backgrounds/contest/wood.xml</filename>
   <options>zoom</options>
 </wallpaper>
</wallpapers>
'''

chemin = "/home/martin/Pictures/listePhotos.xml"
fichierXML = open(chemin, "w")
fichierPhotos = open("/home/martin/Pictures/fonds/liste.txt", "r")

fichierXML.write('<?xml version="1.0" ?>\n')
fichierXML.write('<background>\n')

cheminPhoto = fichierPhotos.readline().replace("\n", "")
cheminPhoto1 = cheminPhoto

while cheminPhoto:
        fichierXML.write('  <static>\n')
        fichierXML.write('    <duration>600</duration>\n')
        fichierXML.write('    <file>{}</file>\n'.format("/home/martin/Pictures/fonds/" + cheminPhoto))
        fichierXML.write('  </static>\n')
        fichierXML.write('  <transition>\n')
        fichierXML.write('      <duration>0.5</duration>\n')
        fichierXML.write('      <from>{}</from>\n'.format("/home/martin/Pictures/fonds/" + cheminPhoto))
        cheminPhoto = fichierPhotos.readline().replace("\n", "")
        if not cheminPhoto:
            cheminPhoto = cheminPhoto1
            fichierXML.write('      <to>{}</to>\n'.format("/home/martin/Pictures/fonds/" + cheminPhoto))
            fichierXML.write('  </transition>\n')
            cheminPhoto = ""
            break
        fichierXML.write('      <to>{}</to>\n'.format("/home/martin/Pictures/fonds/" + cheminPhoto))
        fichierXML.write('  </transition>\n')

fichierPhotos.close()
fichierXML.write("</background>\n")
fichierXML.close()
