# # # import speech_recognition as sr
# # # import os
# # # import tempfile
# # # import sys
# # # import pandas as pd
# # # from sklearn.feature_extraction.text import TfidfVectorizer
# # # from sklearn.naive_bayes import MultinomialNB
# # # from sklearn.model_selection import train_test_split

# # # class AudioTranscriber:
# # #     def __init__(self, dataset_path):
# # #         self.recognizer = sr.Recognizer()
# # #         self.dataset_path = dataset_path

# # #         # Load or initialize dataset
# # #         if os.path.exists(self.dataset_path):
# # #             self.dataset = pd.read_csv(self.dataset_path)
# # #         else:
# # #             self.dataset = pd.DataFrame(columns=["Transcription", "Prediction", "AudioFilePath"])

# # #         # Directory for storing audio and output text
# # #         self.user_home = os.path.expanduser("~")
# # #         self.output_dir = os.path.join(self.user_home, "Documents", "speech_to_text_output")
# # #         self.audio_dir = os.path.join(self.output_dir, "audio_files")
        
# # #         if not os.path.exists(self.audio_dir):
# # #             os.makedirs(self.audio_dir)
# # #         print(f"Using directory: {self.output_dir}")

# # #         # Initialize classification components
# # #         self.vectorizer = TfidfVectorizer()
# # #         self.classifier = MultinomialNB()
# # #         self.model_trained = False
# # #         self.train_model()

# # #     def train_model(self):
# # #         """Train text classification model."""
# # #         if not self.dataset.empty:
# # #             X = self.dataset["Transcription"]
# # #             y = self.dataset["Prediction"]
# # #             X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
            
# # #             if not X_train.empty:
# # #                 X_train_tfidf = self.vectorizer.fit_transform(X_train)
# # #                 self.classifier.fit(X_train_tfidf, y_train)
# # #                 self.model_trained = True
# # #                 print("Classification model trained.")
# # #             else:
# # #                 print("No training data available. Skipping classification model training.")
# # #         else:
# # #             print("Dataset is empty. Skipping classification model training.")

# # #     def classify_text(self, text):
# # #         """Predict location from transcribed text."""
# # #         if not self.model_trained:
# # #             print("Classification model is not trained. Unable to classify text.")
# # #             return "Unknown"
        
# # #         try:
# # #             X_tfidf = self.vectorizer.transform([text])
# # #             prediction = self.classifier.predict(X_tfidf)[0]
# # #             print(f"Predicted location: {prediction}")
# # #             return prediction
# # #         except Exception as e:
# # #             print(f"Error in classification: {e}")
# # #             return "Unknown"

# # #     def save_audio(self, audio_data):
# # #         """Save audio data to file."""
# # #         temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False, dir=self.audio_dir)
# # #         with open(temp_file.name, "wb") as f:
# # #             f.write(audio_data.get_wav_data())
# # #         return temp_file.name

# # #     def transcribe_live_audio(self):
# # #         """Capture and transcribe live audio."""
# # #         try:
# # #             with sr.Microphone() as source:
# # #                 print("\nAdjusting for ambient noise... Please wait.")
# # #                 self.recognizer.adjust_for_ambient_noise(source, duration=2)
# # #                 print("Listening... Speak something:")
# # #                 audio_data = self.recognizer.listen(source)

# # #                 # Transcription
# # #                 text = self.recognizer.recognize_google(audio_data)
# # #                 print("\nTranscribed text:", text)

# # #                 # Save audio and classify
# # #                 audio_path = self.save_audio(audio_data)
# # #                 prediction = self.classify_text(text)

# # #                 # Update dataset
# # #                 new_row = pd.DataFrame({
# # #                     "Transcription": [text],
# # #                     "Prediction": [prediction],
# # #                     "AudioFilePath": [audio_path]
# # #                 })
# # #                 self.dataset = pd.concat([self.dataset, new_row], ignore_index=True)
# # #                 self.dataset.to_csv(self.dataset_path, index=False)

# # #                 return text, prediction
# # #         except sr.UnknownValueError:
# # #             print("Speech recognition could not understand the audio")
# # #         except sr.RequestError as e:
# # #             print(f"Could not request results from speech recognition service; {e}")
# # #         except Exception as e:
# # #             print(f"Error during transcription: {e}")
# # #             return None, None

# # # def check_microphone():
# # #     """Test microphone access."""
# # #     try:
# # #         mic_list = sr.Microphone.list_microphone_names()
# # #         print("\nAvailable microphones:")
# # #         for i, mic in enumerate(mic_list):
# # #             print(f"{i}: {mic}")
# # #         return True
# # #     except Exception as e:
# # #         print(f"Error accessing microphones: {e}")
# # #         return False

# # # def main():
# # #     dataset_path = "/mnt/data/REGIONAL DATASET(Sheet1).csv"

# # #     # Check microphone
# # #     print("Checking microphone...")
# # #     if not check_microphone():
# # #         print("Please check your microphone connection and permissions.")
# # #         sys.exit(1)
    
# # #     print("\nStarting audio transcription...")
# # #     transcriber = AudioTranscriber(dataset_path)

# # #     while True:
# # #         try:
# # #             text, prediction = transcriber.transcribe_live_audio()
# # #             if text:
# # #                 print(f"Transcription: {text}\nPrediction: {prediction}")
# # #                 print("\nWould you like to transcribe more? (yes/no)")
# # #                 response = input().lower()
# # #                 if response != 'yes':
# # #                     break
# # #             else:
# # #                 print("\nWould you like to try again? (yes/no)")
# # #                 response = input().lower()
# # #                 if response != 'yes':
# # #                     break
                
# # #         except KeyboardInterrupt:
# # #             print("\nTranscription stopped by user.")
# # #             break
# # #         except Exception as e:
# # #             print(f"\nAn error occurred: {e}")
# # #             break

# # # if __name__ == "__main__":
# # #     main()
# # import speech_recognition as sr
# # import os
# # import tempfile
# # import sys
# # import pandas as pd
# # from sklearn.feature_extraction.text import TfidfVectorizer
# # from sklearn.naive_bayes import MultinomialNB
# # from sklearn.model_selection import train_test_split

# # class AudioTranscriber:
# #     def __init__(self, dataset_path):
# #         self.recognizer = sr.Recognizer()
# #         self.dataset_path = dataset_path

# #         # Load or initialize dataset
# #         if os.path.exists(self.dataset_path):
# #             self.dataset = pd.read_excel(self.dataset_path)
# #         else:
# #             self.dataset = pd.DataFrame(columns=["Transcription", "Prediction", "AudioFilePath"])

# #         # Directory for storing audio and output text
# #         self.user_home = os.path.expanduser("~")
# #         self.output_dir = os.path.join(self.user_home, "Documents", "speech_to_text_output")
# #         self.audio_dir = os.path.join(self.output_dir, "audio_files")
        
# #         if not os.path.exists(self.audio_dir):
# #             os.makedirs(self.audio_dir)
# #         print(f"Using directory: {self.output_dir}")

# #         # Initialize classification components
# #         self.vectorizer = TfidfVectorizer()
# #         self.classifier = MultinomialNB()
# #         self.model_trained = False
# #         self.train_model()

# #     def train_model(self):
# #         """Train text classification model."""
# #         if not self.dataset.empty:
# #             X = self.dataset["Transcription"]
# #             y = self.dataset["Prediction"]
# #             X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
            
# #             if not X_train.empty:
# #                 X_train_tfidf = self.vectorizer.fit_transform(X_train)
# #                 self.classifier.fit(X_train_tfidf, y_train)
# #                 self.model_trained = True
# #                 print("Classification model trained.")
# #             else:
# #                 print("No training data available. Skipping classification model training.")
# #         else:
# #             print("Dataset is empty. Skipping classification model training.")

# #     def classify_text(self, text):
# #         """Predict location from transcribed text."""
# #         if not self.model_trained:
# #             print("Classification model is not trained. Unable to classify text.")
# #             return "Unknown"
        
# #         try:
# #             X_tfidf = self.vectorizer.transform([text])
# #             prediction = self.classifier.predict(X_tfidf)[0]
# #             print(f"Predicted location: {prediction}")
# #             return prediction
# #         except Exception as e:
# #             print(f"Error in classification: {e}")
# #             return "Unknown"

# #     def save_audio(self, audio_data):
# #         """Save audio data to file."""
# #         temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False, dir=self.audio_dir)
# #         with open(temp_file.name, "wb") as f:
# #             f.write(audio_data.get_wav_data())
# #         return temp_file.name

# #     def transcribe_live_audio(self):
# #         """Capture and transcribe live audio."""
# #         try:
# #             with sr.Microphone() as source:
# #                 print("\nAdjusting for ambient noise... Please wait.")
# #                 self.recognizer.adjust_for_ambient_noise(source, duration=2)
# #                 print("Listening... Speak something:")
# #                 audio_data = self.recognizer.listen(source)

# #                 # Transcription
# #                 text = self.recognizer.recognize_google(audio_data)
# #                 print("\nTranscribed text:", text)

# #                 # Save audio and classify
# #                 audio_path = self.save_audio(audio_data)
# #                 prediction = self.classify_text(text)

# #                 # Update dataset
# #                 new_row = pd.DataFrame({
# #                     "Transcription": [text],
# #                     "Prediction": [prediction],
# #                     "AudioFilePath": [audio_path]
# #                 })
# #                 self.dataset = pd.concat([self.dataset, new_row], ignore_index=True)
# #                 self.dataset.to_excel(self.dataset_path, index=False)

# #                 return text, prediction
# #         except sr.UnknownValueError:
# #             print("Speech recognition could not understand the audio")
# #         except sr.RequestError as e:
# #             print(f"Could not request results from speech recognition service; {e}")
# #         except Exception as e:
# #             print(f"Error during transcription: {e}")
# #             return None, None

# # def check_microphone():
# #     """Test microphone access."""
# #     try:
# #         mic_list = sr.Microphone.list_microphone_names()
# #         print("\nAvailable microphones:")
# #         for i, mic in enumerate(mic_list):
# #             print(f"{i}: {mic}")
# #         return True
# #     except Exception as e:
# #         print(f"Error accessing microphones: {e}")
# #         return False

# # def main():
# #     dataset_path = "/mnt/data/voice_dataset.xlsx"

# #     # Check microphone
# #     print("Checking microphone...")
# #     if not check_microphone():
# #         print("Please check your microphone connection and permissions.")
# #         sys.exit(1)
    
# #     print("\nStarting audio transcription...")
# #     transcriber = AudioTranscriber(dataset_path)

# #     while True:
# #         try:
# #             text, prediction = transcriber.transcribe_live_audio()
# #             if text:
# #                 print(f"Transcription: {text}\nPrediction: {prediction}")
# #                 print("\nWould you like to transcribe more? (yes/no)")
# #                 response = input().lower()
# #                 if response != 'yes':
# #                     break
# #             else:
# #                 print("\nWould you like to try again? (yes/no)")
# #                 response = input().lower()
# #                 if response != 'yes':
# #                     break
                
# #         except KeyboardInterrupt:
# #             print("\nTranscription stopped by user.")
# #             break
# #         except Exception as e:
# #             print(f"\nAn error occurred: {e}")
# #             break

# # if __name__ == "__main__":
# #     main()
# import speech_recognition as sr
# import os
# import tempfile
# import sys
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_selection import train_test_split

# class AudioTranscriber:
#     def __init__(self, dataset_path):
#         self.recognizer = sr.Recognizer()
#         self.dataset_path = dataset_path

#         # Load or initialize dataset
#         if os.path.exists(self.dataset_path):
#             self.dataset = pd.read_excel(self.dataset_path)
#         else:
#             self.dataset = pd.DataFrame(columns=["Transcription", "Prediction", "AudioFilePath"])

#         # Directory for storing audio and output text
#         self.user_home = os.path.expanduser("~")
#         self.output_dir = os.path.join(self.user_home, "Documents", "speech_to_text_output")
#         self.audio_dir = os.path.join(self.output_dir, "audio_files")
        
#         if not os.path.exists(self.audio_dir):
#             os.makedirs(self.audio_dir)
#         print(f"Using directory: {self.output_dir}")

#         # Initialize classification components
#         self.vectorizer = TfidfVectorizer()
#         self.classifier = MultinomialNB()
#         self.model_trained = False
#         self.train_model()

#     def train_model(self):
#         """Train text classification model."""
#         if not self.dataset.empty:
#             X = self.dataset["Transcription"]
#             y = self.dataset["Prediction"]
#             X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
            
#             if not X_train.empty:
#                 X_train_tfidf = self.vectorizer.fit_transform(X_train)
#                 self.classifier.fit(X_train_tfidf, y_train)
#                 self.model_trained = True
#                 print("Classification model trained.")
#             else:
#                 print("No training data available. Skipping classification model training.")
#         else:
#             print("Dataset is empty. Skipping classification model training.")

#     def classify_text(self, text):
#         """Predict location from transcribed text."""
#         if not self.model_trained:
#             print("Classification model is not trained. Unable to classify text.")
#             return "Unknown"
        
#         try:
#             X_tfidf = self.vectorizer.transform([text])
#             prediction = self.classifier.predict(X_tfidf)[0]
#             print(f"Predicted location: {prediction}")
#             return prediction
#         except Exception as e:
#             print(f"Error in classification: {e}")
#             return "Unknown"

#     def save_audio(self, audio_data):
#         """Save audio data to file."""
#         temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False, dir=self.audio_dir)
#         with open(temp_file.name, "wb") as f:
#             f.write(audio_data.get_wav_data())
#         return temp_file.name

#     def transcribe_live_audio(self):
#         """Capture and transcribe live audio."""
#         try:
#             with sr.Microphone() as source:
#                 print("\nAdjusting for ambient noise... Please wait.")
#                 self.recognizer.adjust_for_ambient_noise(source, duration=2)
#                 print("Listening... Speak something:")
#                 audio_data = self.recognizer.listen(source)

#                 # Transcription
#                 text = self.recognizer.recognize_google(audio_data)
#                 print("\nTranscribed text:", text)

#                 # Save audio and classify
#                 audio_path = self.save_audio(audio_data)
#                 prediction = self.classify_text(text)

#                 # Update dataset
#                 new_row = pd.DataFrame({
#                     "Transcription": [text],
#                     "Prediction": [prediction],
#                     "AudioFilePath": [audio_path]
#                 })
#                 self.dataset = pd.concat([self.dataset, new_row], ignore_index=True)
#                 self.dataset.to_excel(self.dataset_path, index=False)

#                 return text, prediction
#         except sr.UnknownValueError:
#             print("Speech recognition could not understand the audio")
#         except sr.RequestError as e:
#             print(f"Could not request results from speech recognition service; {e}")
#         except Exception as e:
#             print(f"Error during transcription: {e}")
#             return None, None

# def check_microphone():
#     """Test microphone access."""
#     try:
#         mic_list = sr.Microphone.list_microphone_names()
#         print("\nAvailable microphones:")
#         for i, mic in enumerate(mic_list):
#             print(f"{i}: {mic}")
#         return True
#     except Exception as e:
#         print(f"Error accessing microphones: {e}")
#         return False

# def main():
#     dataset_path = os.path.expanduser("~/Documents/speech_to_text_output/voice_dataset.xlsx")

#     # Check microphone
#     print("Checking microphone...")
#     if not check_microphone():
#         print("Please check your microphone connection and permissions.")
#         sys.exit(1)
    
#     print("\nStarting audio transcription...")
#     transcriber = AudioTranscriber(dataset_path)

#     while True:
#         try:
#             text, prediction = transcriber.transcribe_live_audio()
#             if text:
#                 print(f"Transcription: {text}\nPrediction: {prediction}")
#                 print("\nWould you like to transcribe more? (yes/no)")
#                 response = input().lower()
#                 if response != 'yes':
#                     break
#             else:
#                 print("\nWould you like to try again? (yes/no)")
#                 response = input().lower()
#                 if response != 'yes':
#                     break
                
#         except KeyboardInterrupt:
#             print("\nTranscription stopped by user.")
#             break
#         except Exception as e:
#             print(f"\nAn error occurred: {e}")
#             break

# if __name__ == "__main__":
#     main()
# import speech_recognition as sr
# import spacy

# # Dictionary data
data = {
  "Anakapalli": ["Anakapalli", "Bheemunipatnam", "Bowluvada", "Butchayyapeta", "Cheedikada", "Chodavaram", "Devarapalli", "Elamanchili", "Golugonda", "K. Kotapadu", "Kantabamsuguda", "Kasimkota", "Madugula", "Makavarapalem", "Munagapaka", "Nakkapalle", "Narsipatnam", "Narsipatnam revenue division", "Nathavaram", "Paravada", "Payakaraopeta", "Rambilli", "Ravikamatham", "Rolugunta", "Sabbavaram", "S. Rayavaram", "Vizianagaram", "Yellamanchili"],
  "Anantapuramu": ["Adoni", "Amarapuram", "Anantapur", "Antakal", "Anugula", "Atmakur", "Bathalapalle", "Beluguppa", "Bukkapatnam", "Brahmanapalle", "Byrampuram", "Challakere", "Chilamathur", "Chinna Manchikonda", "Chinna Veeranagallu", "Chitravati", "Cuddapah", "Dharmavaram", "Dhone", "Donakonda", "Gooty", "Gummagatta", "Hindupur", "Hirehalli", "Hospet", "Kadiri", "Kalyandurgam", "Kamalapuram", "Kanaganapalli", "Kurnool", "Madakasira", "Madanapalle", "Mantralayam", "Muddenahalli", "Nandyal", "Nemili", "Penukonda", "Puttaparthi", "Rayachoty", "Santhapuram", "Singanamala", "Tadipatri", "Uravakonda", "Vaddadi", "Vaddamanu", "Vinukonda", "Guntakal", "PamidiNagar", "Rayadurg"],
  "Annamayya": ["Beerangi Kothakota", "Kalikiri", "Kurabalakota", "Madanapalle", "Mulakalacheruvu", "Nimmanapalle", "Peddamandyam", "Peddathippasamudram", "Ramasamudram", "Thamballapalle", "Valmikipuram", "Chitvel", "Nandalur", "Obulavaripalle", "Penagalur", "Pullampeta", "Railway Koduru", "Rajampet", "T. Sundupalle", "Veeraballi", "Chinnamandyam", "Galiveedu", "Gurramkonda", "Kalakada", "Kambhamvaripalle", "Lakkireddypalli", "Pileru", "Ramapuram", "Rayachoti", "Sambepalli"],
  "Alluri Sitharama Raju": ["Chinturu", "Etapaka", "Kunavaram", "Vararamachandrapuram", "Ananthagiri", "Araku Valley", "Chintapalli", "Dumbriguda", "Ganagaraju Madugula", "Gudem Kotha Veedhi", "Hukumpeta", "Koyyuru", "Munchingi Puttu", "Paderu", "Peda Bayalu", "Addateegala", "Devipatnam", "Gangavaram", "Maredumilli", "Rajavommangi", "Rampachodavaram", "Y. Ramavaram"],
  "Bapatla": ["Bapatla", "Karlapalem", "Martur", "Parchur", "Pittalavanipalem", "Yeddanapudi", "Addanki", "Ballikurava", "Chinaganjam", "Chirala", "Inkollu", "J. Panguluru", "Karamchedu", "Korisapadu", "Santhamaguluru", "Vetapalem", "Amruthalur", "Bhattiprolu", "Cherukupalle", "Kollur", "Nagaram", "Nizampatnam", "Repalle", "Tsundur", "Vemuru"],
  "Chittoor": ["Chittoor Rural", "Chittoor Urban", "Gangadhara Nellore", "Gudipala", "Irala", "Penumuru", "Pulicherla", "Puthalapattu", "Rompicherla", "Srirangarajapuram", "Thavanampalle", "Vedurukuppam", "Yadamari", "Gudupalle", "Kuppam", "Ramakuppam", "Santhipuram", "Karvetinagar", "Nagari", "Nindra", "Palasamudram", "Vijayapuram", "Baireddipalle", "Bangarupalyam", "Chowdepalle", "Gangavaram", "Palamaner", "Peddapanjani", "Punganur", "Sodam", "Somala", "Venkatagirikota"],
  "East Godavari": ["Rajamahendravaram", "Kadiam", "Rajanagaram", "Seethanagaram", "Korukonda", "Anaparthi", "Biccavolu", "Rangampeta", "Gokavaram", "Kovvuru", "Chagallu", "Tallapudi", "Nidadavole", "Undrajavaram", "Peravali", "Devarapalle", "Nallajerla", "Gopalapuram"],
  "Eluru": ["Bhimadole", "Denduluru", "Eluru", "Kaikalur", "Kalidindi", "Mandavalli", "Mudinepalli", "Nidamarru", "Pedapadu", "Pedavegi", "Buttayagudem", "Dwaraka Tirumala", "Jangareddygudem", "Jeelugu Milli", "Kamavarapukota", "Koyyalagudem", "Kukunuru", "Polavaram", "T. Narasapuram", "Velairpadu", "Agiripalli", "Chatrai", "Chintalapudi", "Lingapalem", "Musunuru", "Nuzvid"],
  "Guntur": ["Guntur","Guntur East", "Guntur West", "Medikonduru", "Pedakakani", "Pedanandipadu", "Phirangipuram", "Prathipadu", "Tadikonda", "Thullur", "Vatticherukuru", "Chebrolu", "Duggirala", "Kakumanu", "Kollipara", "Mangalagiri", "Ponnur", "Tadepalle", "Tenali"],
  "Kakinada": ["Samalkota", "Pithapuram", "Gollaprolu", "U. Kothapalli", "Karapa", "Kakinada Rural", "Kakinada Urban", "Pedapudi", "Thallarevu", "Kajuluru", "Peddapuram", "Jaggampeta", "Gandepalle", "Kirlampudi", "Tuni", "Kotananduru", "Prathipadu", "Sankhavaram", "Yeleswaram", "Rowthulapudi", "Thondangi"],
  "Konaseema": ["Allavaram", "Amalapuram", "I. Polavaram", "Katrenikona", "Malikipuram", "Mamidikuduru", "Mummidivaram", "Razole", "Sakhinetipalle", "Uppalaguptam", "Ainavilli", "Alumuru", "Ambajipeta", "Atreyapuram", "Kothapeta", "P. Gannavaram", "Ravulapalem", "Gangavaram", "Kapileswarapuram", "Mandapeta", "Rayavaram", "Ramachandrapuram"],
  "Krishna": ["Bapulapadu", "Gannavaram", "Gudivada", "Gudlavalleru", "Nandivada", "Pedaparupudi", "Unguturu", "Avanigadda", "Bantumilli", "Challapalli", "Ghantasala", "Guduru", "Koduru", "Kruthivennu", "Machilipatnam North", "Machilipatnam South", "Mopidevi", "Nagayalanka", "Pedana", "Kankipadu", "Movva", "Pamarru", "Pamidimukkala", "Penamaluru", "Thotlavalluru", "Vuyyuru"],
  "Kurnool": ["Adoni", "Gonegandla", "Holagunda", "Kosigi", "Kowthalam", "Mantralayam", "Nandavaram", "Pedda Kadabur", "Yemmiganur", "C. Belagal", "Gudur", "Kallur", "Kodumur", "Kurnool Rural", "Kurnool Urban", "Orvakal", "Veldurthi", "Alur", "Aspari", "Chippagiri", "Devanakonda", "Halaharvi", "Krishnagiri", "Maddikera East", "Pattikonda", "Tuggali"], 
  "Nandyal": ["Atmakur", "Bandi Atmakur", "Jupadu Bunglow", "Kothapalle", "Miduthuru", "Nandikotkur", "Pagidyala", "Pamulapadu", "Srisailam", "Velugodu", "Banaganapalli", "Bethamcherla", "Dhone", "Koilkuntla", "Owk", "Peapully", "Allagadda", "Chagalamarri", "Dornipadu", "Gadivemula", "Gospadu", "Kolimigundla", "Mahanandi", "Nandyal Rural", "Nandyal Urban", "Panyam", "Rudravaram", "Sanjamala", "Sirivella", "Uyyalawada"],
  "Nellore": ["Ananthasagaram", "Anumasamudrampeta", "Atmakur", "Chejerla", "Kaluvoya", "Marripadu", "Sangam", "Seetharamapuram", "Udayagiri", "Gudluru", "Kandukur", "Kondapuram", "Lingasamudram", "Ulavapadu", "Varikuntapadu", "Voletivaripalem", "Allur", "Bogole", "Dagadarthi", "Duttalur", "Jaladanki", "Kaligiri", "Kavali", "Kodavalur", "Vidavalur", "Vinjamur", "Buchireddipalem", "Indukurpet", "Kovur", "Manubolu", "Muthukur", "Nellore Rural", "Nellore Urban", "Podalakur", "Rapur", "Sydapuram", "Thotapalli Gudur", "Venkatachalam"], 
  "NTR": ["Chandarlapadu", "Jaggayyapeta", "Kanchikacherla", "Nandigama", "Penuganchiprolu", "Vatsavai", "Veerullapadu", "A. Konduru", "Gampalagudem", "Reddigudem", "Tiruvuru", "Vissannapeta", "G. Konduru", "Ibrahimpatnam", "Mylavaram", "Vijayawada Rural", "Vijayawada Central", "Vijayawada North", "Vijayawada East", "Vijayawada West"],
   "Palnadu": ["Dachepalle", "Durgi", "Gurazala", "Karempudi", "Machavaram", "Macherla", "Piduguralla", "Rentachintala", "Veldurthi", "Bollapalle", "Chilakaluripeta", "Edlapadu", "Ipur", "Nadendla", "Narasaraopet", "Nuzendla", "Rompicherla", "Savalyapuram", "Vinukonda", "Amaravathi", "Atchampet", "Bellamkonda", "Krosuru", "Muppalla", "Nekarikallu", "Pedakurapadu", "Rajupalem", "Sattenapalli"], 
   "Parvathipuram Manyam": ["Jiyyammavalasa", "Gummalaxmipuram", "Kurupam", "Palakonda", "Seethampeta", "Bhamini", "Veeraghattam", "Parvathipuram", "Seethanagaram", "Balijipeta", "Salur", "Panchipenta", "Makkuva", "Komarada", "Garugubilli"], 
   "Prakasam": ["Chandrasekharapuram", "Darsi", "Donakonda", "Hanumanthunipadu", "Kanigiri", "Konakanamitla", "Kurichedu", "Marripudi", "Pamur", "Pedacherlopalle", "Podili", "Ponnaluru", "Veligandla", "Ardhaveedu", "Bestavaripeta", "Cumbum", "Dornala", "Giddalur", "Komarolu", "Markapuram", "Pedda Araveedu", "Pullalacheruvu", "Racherla", "Tarlupadu", "Tripuranthakam", "Yerragondapalem", "Chimakurthy", "Kondapi", "Kothapatnam", "Maddipadu", "Mundlamuru", "Naguluppalapadu", "Ongole Rural", "Ongole Urban", "Santhanuthalapadu", "Singarayakonda", "Tanguturu", "Thallur", "Zarugumalli"], 
   "Rayalaseema": ["Anantapur", "Guntakal", "Hindupur", "Kadiri", "Rayadurg", "Tadipatri", "Dharmavaram", "Kalyandurg"], "Srikakulam": ["Ichchapuram", "Kaviti", "Sompeta", "Kanchili", "Palasa", "Mandasa", "Vajrapukotturu", "Nandigama", "Srikakulam", "Gara", "Amadalavalasa", "Ponduru", "Sarubujjili", "Burja", "Narasannapeta", "Polaki", "Etcherla", "Laveru", "Ranastalam", "Ganguvarisigadam", "Jalumuru", "Tekkali", "Santha Bommali", "Kotabommali", "Pathapatnam", "Meliaputti", "Saravakota", "Kothuru", "Hiramandalam", "Lakshminarasupeta"], 
   "Sri Sathya Sai": ["Bathalapalle", "Chennekothapalle", "Dharmavaram", "Kanaganapalle", "Mudigubba", "Ramagiri", "Tadimarri", "Amadagur", "Gandlapenta", "Kadiri", "Nallacheruvu", "Nambulapulakunta", "Talupula", "Tanakal", "Agali", "Amarapuram", "Chilamathur", "Gudibanda", "Hindupur", "Lepakshi", "Madakasira", "Parigi", "Penukonda", "Roddam", "Rolla", "Somandepalle", "Bukkapatnam", "Gorantla", "Kothacheruvu", "Nallamada", "Obuladevaracheruvu", "Puttaparthi"], 
   "Tirupati": ["Tirupati","Balayapalli", "Chillakur", "Chittamur", "Dakkili", "Gudur", "Kota", "Vakadu", "Venkatagiri", "K. V. B. Puram", "Nagalapuram", "Narayanavanam", "Pichatur", "Renigunta", "Srikalahasti", "Thottambedu", "Yerpedu", "Buchinaidu Kandriga", "Doravarisatram", "Naidupeta", "Ozili", "Pellakur", "Satyavedu", "Sullurpeta", "Tada", "Varadaiahpalem", "Chandragiri", "Chinnagottigallu", "Pakala", "Puttur", "Ramachandrapuram", "Tirupati Rural", "Tirupati Urban", "Vadamalapeta", "Yerravaripalem"], 
   "Visakhapatnam": ["Bheemunipatnam", "Anandapuram", "Padmanabham", "Visakhapatnam Rural", "Seethammadhara", "Gajuwaka", "Pedagantyada", "Gopalapatnam", "Mulagada", "Maharanipeta", "Pendurthi"],
   "Vizianagaram": ["Bobbili", "Ramabhadrapuram", "Badangi", "Therlam", "Gajapathinagaram", "Dattirajeru", "Mentada", "Cheepurupalli", "Garividi", "Gurla", "Merakamudidam", "Vangara", "Regidi Amadalavalasa", "Santhakavati mandal", "Rajam", "Vizianagaram Urban", "Gantyada", "Poosapatirega", "Denkada", "Bhogapuram", "Srungavarapukota", "Jami", "Vepada", "Lakkavarapukota", "Kothavalasa", "Bondapalli", "Nellimarla", "Vizianagaram Rural"],
  
   "YSR Kadapa": ["Atlur", "B. Kodur", "Badvel", "Bramhamgari Matham", "Chapadu", "Duvvur", "Gopavaram", "Kalasapadu", "Khajipet", "Mydukur", "Porumamilla", "Sri Avadhutha Kasinayana", "Jammalamadugu", "Kondapuram", "Muddanur", "Mylavaram", "Peddamudium", "Proddatur", "Rajupalem", "Chennur", "Chinthakommadinne", "Kadapa", "Kamalapuram", "Pendlimarri", "Siddavatam", "Vallur", "Vontimitta", "Yerraguntla", "Chakarayapet", "Lingala", "Pulivendula", "Simhadripuram", "Thondur", "Veerapunayunipalle", "Vempalle", "Vemula"] 
}


# # Load the NER model
# nlp = spacy.load("en_core_web_sm")  # Replace with a custom model if available

# def predict_district(transcribed_text):
#     """Identify the district based on transcribed text."""
#     doc = nlp(transcribed_text)
#     detected_entities = [ent.text for ent in doc.ents]

#     for entity in detected_entities:
#         for district, locations in data.items():
#             if entity in locations:
#                 return f"Detected: {entity} -> District: {district}"

#     return "No matching district found."

# def recognize_speech():
#     """Capture live voice input and process."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening... Speak now:")
#         recognizer.adjust_for_ambient_noise(source)
#         try:
#             audio = recognizer.listen(source)
#             print("Processing your input...")
#             # Transcribe the audio
#             transcribed_text = recognizer.recognize_google(audio)
#             print(f"Transcribed Text: {transcribed_text}")
#             return transcribed_text
#         except sr.UnknownValueError:
#             print("Sorry, could not understand the audio.")
#         except sr.RequestError as e:
#             print(f"Error with the speech recognition service: {e}")

# def main():
#     """Main function to run the live prediction."""
#     print("Welcome to the live voice prediction system.")
#     while True:
#         # Get live input from the user
#         transcribed_text = recognize_speech()
#         if transcribed_text:
#             # Predict based on transcribed input
#             result = predict_district(transcribed_text)
#             print(result)

#         # Option to exit
#         exit_input = input("Do you want to continue? (yes/no): ").strip().lower()
#         if exit_input == "no":
#             print("Exiting the program.")
#             break

# if __name__ == "__main__":
#     main()
import speech_recognition as sr
import spacy

# Dictionary data


# Load the NER model
nlp = spacy.load("en_core_web_sm")

def predict_district(transcribed_text):
    """Identify the district based on transcribed text."""
    doc = nlp(transcribed_text)
    detected_entities = [ent.text for ent in doc.ents]

    # Tokenize transcribed text into individual words
    tokens = transcribed_text.lower().split()

    print(f"Detected tokens: {tokens}")  # Debugging

    for token in tokens:
        token = token.strip()  # Normalize the token
        for district, locations in data.items():
            for location in locations:
                if token == location.lower().strip():
                    return f"Detected: {token} -> District: {district}"
    return "No matching district found."

def recognize_speech_live():
    """Capture live voice input and process."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now:")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            print("Processing your input...")
            # Transcribe the audio
            transcribed_text = recognizer.recognize_google(audio)
            print(f"Transcribed Text: {transcribed_text}")
            return transcribed_text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
    return None

def recognize_speech_file(file_path):
    """Process speech from an audio file."""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            print("Processing the audio file...")
            audio = recognizer.record(source)
            # Transcribe the audio
            transcribed_text = recognizer.recognize_google(audio)
            print(f"Transcribed Text: {transcribed_text}")
            return transcribed_text
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
    return None

def main():
    """Main function to run the program."""
    print("Welcome to the district prediction system.")
    print("Choose an option:")
    print("1. Live audio input")
    print("2. Audio file input")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            transcribed_text = recognize_speech_live()
        elif choice == '2':
            file_path = input("Enter the path to the audio file: ")
            transcribed_text = recognize_speech_file(file_path)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        if transcribed_text:
            result = predict_district(transcribed_text)
            print(result)

if __name__ == "__main__":
    main()
