import json 

with open("sounds.json") as json_file:
    data = json.load(json_file)
    outfile = open("sound_out.md", "w+")

    #Collect sounds for the linker
    save = ""
    mob = ""
    for sound in data:
        current = sound.split(".")[0]
        mob_current = sound.split(".")[1]
        if(save != current):
            outfile.write(" - [{0}](#{0})\n".format(current))
            save = current
        if(current == "mob" and mob != mob_current):
            mob = mob_current
            outfile.write("   - [{0}](#{0})\n".format(mob_current))

    id = ""
    mob = ""

    for sound in data:
        current = sound.split(".")[0]
        mob_current = sound.split(".")[1]
        if(id != current):
            outfile.write("# " + current + "\n\n")
            id = current
        if(id == "mob" and mob != mob_current):
            mob = mob_current
            outfile.write("## " + mob_current + "\n\n")

        outfile.write("`" + sound + "`\n\n")

