class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        temp = hash(longUrl)
        self.d = {}
        self.d[temp] = longUrl
        short_url = "http://tinyurl.com/" + str(temp)
        return short_url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        shortUrl = shortUrl.split("/")
        temp = int(shortUrl[-1])
        return self.d[temp]


obj = Codec()
assert "http://tinyurl.com/4690931709257052457" == obj.encode("https://leetcode.com/problems/encode-and-decode-tinyurl/")
assert "https://leetcode.com/problems/encode-and-decode-tinyurl/" == obj.decode("http://tinyurl.com/4690931709257052457")
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
