import string
import re
import joblib

# PREPROCESSING
punc = string.punctuation
abbv = {
    "AFAIK":"as far as I know",
	"IMO":	"in my opinion",
	"IMHO":	"in my humble opinion",
	"LGTM":	"look good to me",
	"AKA":	"also know as",
	"ASAP":	"as sone as possible",
	"BTW":	"by the way",
	"FAQ":	"frequently asked questions",
	"DIY":	"do it yourself",
	"DM":	"direct message",
	"FYI":	"for your information",
	"IC":	"i see",
	"IOW":	"in other words",
	"IIRC":	"If I Remember Correctly",
	"icymi":"In case you missed it",
	"CUZ":	"because",
	"COS":	"because",
	"nv":	"nevermind",
	"PLZ":	"please",
}
html_pattern = re.compile('<.*?>')
urls_pattern = re.compile(r'https?://\S+|www\.\S+')
emoji_pattern = re.compile("["
	u"\U0001F600-\U0001F64F"  # emoticons
	u"\U0001F300-\U0001F5FF"  # symbols & pictographs
	u"\U0001F680-\U0001F6FF"  # transport & map symbols
	u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
"]+", flags=re.UNICODE)

# PIPELINE
pipeline = joblib.load("./src/movie_reviews/pipeline.pkl")

def predict(text):
	cleaned = preprocess(text)
	pred = pipeline.predict([cleaned])[0]
	output = [0, 0]
	output[pred] = 0.8
	output[1-pred] = 0.2
	return output

def preprocess(text):
    text = text.lower()	# Lowercase
    text = html_pattern.sub(r'', text)	# HTML Tags
    text = urls_pattern.sub(r'', text)	# urls
    text = text.translate(str.maketrans("", "", punc))	# punctuations
    text = emoji_pattern.sub(r'', text)	# Emojis
    new_text = []
    for word in text.split(" "):
        word = abbv.get(word.upper(), word)	# abbreviations
        new_text.append(word)
    text = " ".join(new_text)
    return text