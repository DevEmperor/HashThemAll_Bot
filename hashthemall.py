import discord
import hashfunctions

channel_name = 'my_hashthemall_bot'  # ENTER THE CHANNEL'S NAME HERE, ON WHICH THE BOT SHOULD LISTEN
token = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg'  # ENTER YOUR APPLICATION-TOKEN HERE

bot = discord.Client


class HashThemAll_Bot(bot):

    async def on_ready(self):
        print("[Bot] I logged myself in. Beep bop!")

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.channel == discord.utils.get(bot.get_all_channels(self), name=channel_name):
            await message.delete()

            text = message.content

            await message.author.send("Calculating...")

            md4_hash = hashfunctions.calc_md4(text)
            md5_hash = hashfunctions.calc_md5(text)
            sha1_hash = hashfunctions.calc_sha1(text)
            sha224_hash = hashfunctions.calc_sha224(text)
            sha256_hash = hashfunctions.calc_sha256(text)
            sha384_hash = hashfunctions.calc_sha384(text)
            sha512_hash = hashfunctions.calc_sha512(text)
            sha3_224_hash = hashfunctions.calc_sha3_224(text)
            sha3_256_hash = hashfunctions.calc_sha3_256(text)
            sha3_384_hash = hashfunctions.calc_sha3_384(text)
            sha3_512_hash = hashfunctions.calc_sha3_512(text)
            blake2b_hash = hashfunctions.calc_blake2b(text)
            blake2s_hash = hashfunctions.calc_blake2s(text)
            ripemd160_hash = hashfunctions.calc_ripemd160(text)
            whirlpool_hash = hashfunctions.calc_whirlpool(text)
            bcrypt_hash = hashfunctions.calc_bcrypt(text, cost=15)

            await message.author.send(
                "__**HashThemAll calculated the following hashes for your text:**__\n\"" + text + "\"\n"
                + "\n**MD4:**\n" + md4_hash
                + "\n**MD5:**\n" + md5_hash
                + "\n**SHA1:**\n" + sha1_hash
                + "\n**SHA224:**\n" + sha224_hash
                + "\n**SHA256:**\n" + sha256_hash
                + "\n**SHA384:**\n" + sha384_hash
                + "\n**SHA512:**\n" + sha512_hash
                + "\n**SHA3_224:**\n" + sha3_224_hash
                + "\n**SHA3_256:**\n" + sha3_256_hash
                + "\n**SHA3_384:**\n" + sha3_384_hash
                + "\n**SHA3_512:**\n" + sha3_512_hash
                + "\n**BLAKE2B:**\n" + blake2b_hash
                + "\n**BLAKE2S:**\n" + blake2s_hash
                + "\n**RIPEMD160:**\n" + ripemd160_hash
                + "\n**WHIRLPOOL:**\n" + whirlpool_hash
                + "\n**BCRYPT (Cost: 15):**\n" + bcrypt_hash + "\n\n")
            print("[Bot] Calculated the hashes of: \"" + text + "\" !")


client = HashThemAll_Bot()
client.run(token)
