# OCR-Hindi

## Overview

This Flask application provides a simple API for extracting text from uploaded images. Users can submit an image file using a `POST` request to the `/extract-text` endpoint, and the API will return the extracted text in JSON format.

## Setup

### Prerequisites

- Python 3.x
- Flask (`pip install Flask`)
- Tesseract OCR: The heart of our program. As per Wikipedia, it is an OCR tool developed by HP and released to Open Source in 2005. You can download it here:
  
  - For Windows: https://github.com/UB-Mannheim/tesseract/wiki
  
  - For Linux: https://github.com/tesseract-ocr/tesseract
  
  **NOTE: Please note that when asked to Choose components:**

  - Select Additional Script Data, expand it, and select Devanagari script.

    ![img-1](https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4/blob/test/demo-images/ocr-demo/img_1.png)

  - Under Additional Language Data, select Hindi.

    ![img-2](https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4/blob/test/demo-images/ocr-demo/img_2.png)
    
  - Once installed, add the install location: “C:\Program Files\Tesseract-OCR” (for Windows its default)


### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4.git
   cd RJPOLICE_HACK_668_NeuralNomards_4
   ```
2. Create a virtual enviorment and activate it for isolation
   ```bash
   python -m venv test
   ```
   and
   
   ```bash
   .\test\Scripts\activate
   ```
  
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:

   ```bash
   cd ocr
   python ocr.py
   ```

2. Open Postman and create a new request.

3. Set the request type to `POST` and enter the following URL:

   ```
   http://127.0.0.1:5000/extract-text
   ```

4. Switch to the "Body" tab, select the "form-data" option, and add a key-value pair with the key `file` and the value as the image file you want to upload.

5. Click the "Send" button to submit the request.

6. View the response in JSON format, containing the extracted text from the uploaded image.

## API Endpoint

### `POST /extract-text`

- **Description:** Extracts text from the uploaded image.
- **Request Type:** `POST`
- **Request Body:** Form-data with key `file` and the value as the image file.
- **Response Format:** JSON
- **Response Example:**
  ```json
   {
    "text": "N.C.R.B/एन.सी.आर.बी\nI.I.F.-I /एकᳱकृत जाँच फामᭅ-I\nFIRST INFORMATION REPORT\n(Under Section 154 Cr.P.C.)\n2017 गजनेर\n0030बीकानेर\nFIR No.\n(ᮧ.सू.ᳯर.सं):1.District \n(िजला):P.S.\n(थाना):Year\n(वषᭅ):\nभा दं सं 1860 379 1 Acts  \n (अिधिनयम)Sections \n (धाराएँ)S.No.\n(ᮓ.सं.)\nखान एवं खिनज (िवकास का िविनयमन) अिधिनयम 1957 4 2\nखान एवं खिनज (िवकास का िविनयमन) अिधिनयम 1957 21 3\n10:13 बजे30/03/2017\n08:10 बजे30/03/2017\nTime To\n (समय तक):Time From\n(समय से):Time Period\n(समय अविध):Date To\n(ᳰदनांक तक):Date From\n(ᳰदनांक से):Day(ᳰदन):Occurrence of offence (अपराध कᳱ घटना): 3.\n1.\nपहर गुᱨवार(a)\n18:20 बजे 01/04/2017Time\n (समय):Date\n(ᳰदनांक):Information received at P.S.\n(थाना जहाँ सूचना ᮧा᳙ ᱟई):\n01/04/2017 18:20:00 बजे 017Date & Time\n(ᳰदनांक एवं समय) General Diary Reference \n(रोजनामचा संदभᭅ) :(c)\n5.\nBeat No.\n(बीट सं.) :Direction and distance from P.S.\n(थाने से ᳰदशा और दूरी):उᱫर,  3  ᳰकमी(a)1.\n(b)Address(पता): नवोदय फांटा एनएच-15\n(cIn case, outside the limit of this Police Station, then\n(यᳰद थाना सीमा के बाहर हᱹ तो)\nDistrict(State)\n(िजला (रा᭔य) ):Name of P.S\n(थाना का नाम):Place of Occurrence (घटना᭭थल): Type of Information (सूचना का ᮧकार):4. िलिखतEntry No.\n(ᮧिवि᳥ सं.):(b)(ᮧथम सूचना ᳯरपोटᭅ )\n(धारा 154 द᭛ड ᮧᳰᮓया संिहता के तहत)\nDate and Time of FIR \n(एफआईआर कᳱ ितिथ/समय):01/04/2017 18:20 बजे2.\n1N.C.R.B/एन.सी.आर.बी\nI.I.F.-I /एकᳱकृत जाँच फामᭅ-I\n6.Complainant / Informant (िशकायतकताᭅ / सूचनाकताᭅ):\nName(नाम):(a) तीथᭅराज चौहान \n(b)\n(c)Date/Year of Birth \n(ज᭠म ितिथ/ वषᭅ):(d)Nationality(रा᳦ीयता): भारत 1987\n(e)UID No(यूआईडी सं.):\n(f)Passport No. (पासपोटᭅ सं.):\nDate of Issue \n(जारी करने कᳱ ितिथ):Place of Issue\n(जारी करने का ᭭थान):मुरली मनोहर चौहान Father's Name (िपता का नाम):\nS.No.  Id Type Id Number(g)Id details (Ration Card,Voter ID Card,Passport,UID No.,Driving License,PAN) (पहचान िववरण( राशन काडᭅ,\nमतदाता पहचान पᮢ,पारपᮢ,आधार काडᭅ सं,ᮟाइᳲवग लाइसᱶस,पैन)):\n(h)Occupation (᳞वसाय):\nAddress(पता):(i)\n1 ज᭭सुसर गेट के बाहर मािलयो का, नया शहर, बीकानेर, राज᭭थान, भारतS.No. (ᮓ.\nसं.)Address Type\n (पता का ᮧकार)Address \n(पता)\nवतᭅमान पता\nज᭭सुसर गेट के बाहर मािलयो का, नया शहर, बीकानेर, राज᭭थान, भारत 2 ᭭थायी पता\n(j)Phone number\n(दूरभाष न.):Mobile (मोबाइल न.):\n7.Details of known/suspected/unknown accused with full particulars\n(᭄ात/संᳰद᭏ध/अ᭄ात अिभयुᲦ का पुरे िववरण सिहत वणᭅन):\nल᭯मण  1 1. रामपुरा ब᭭ती गली नं20,नया शहर,\nबीकानेर,राज᭭थान,भारत\n9.Particulars of properties of interest (Attach separate sheet, if necessary)\n(स᭥बि᭠धत स᭥पिᱫ का िववरण( यᳰद आव᭫यक हो, तो अलग पृ᳥ न᭜थी करᱶ)):\nS.No.\n (ᮓ.सं.)Property Category \n(स᭥पिᱫ ᮰ेणी)Property Type (स᭥पिᱫ \nके ᮧकार)Description\n (िववरण)Value(In Rs/-)\n(मू᭨य(ᱧ मᱶ))8.Reasons for delay in reporting by the complainant/informant\n(िशकायतकताᭅ / सूचनाकताᭅ ᳇ारा ᳯरपोटᭅ देरी से दजᭅ कराने के कारण):S.No.\n(ᮓ.सं.)Name \n(नाम)Alias\n(उपनाम)Relative's Name\n(ᳯर᭫तेदार का नाम)Address\n(पता)Accused More Than(अ᭄ात आरोपी एक से अिधक हो तो सं᭎या):\n2N.C.R.B/एन.सी.आर.बी\nI.I.F.-I /एकᳱकृत जाँच फामᭅ-I\n10.Total value of property stolen(In Rs/-)\n(चोरी ᱟई संपिᱫ का कुल मू᭨य(ᱧ मᱶ) ):\n11.Inquest Report / U.D. case No., if any (मृ᭜यु समीᭃा ᳯरपोटᭅ / यू.डी.ᮧकरण न., यᳰद कोई हो):\nइस समय ᮰ी तीथᭅराज पुᮢ मुरली मनोहर जाित माली उ᮫ 30साल िनवासी मािलयो का मोह᭨ला ज᭭सुसर गेट के बाहर \nपुिलस थाना नयाशहर िजला बीकानेर हाल एमएफ 2खिनज िवभाग कोलायत िजला बीकानेर ने हािजर थाना होकर एक \nिलिखत ᳯरपोटᭅ बदी मजून,राज᭭थान सरकार सेवा मᱶ ᮰ीमान थानािधकारी पुिलस थाना गजनेर िजला बीकानेर िवषय –\nखिनज िज᭡सम के अवैध खनन/िनगᭅमन के िवᱧ᳍ ᮧथम सूचना ᳯरपोटᭅ दजᭅ करने बाबत। महोदय, उपरोᲦ िवषया᭠तगᭅत \nिनवेदन है ᳰक जᳯरये दूरभाष सूचना ᮧा᳙ होने पर ᮰ीमान सहा. अिभय᭠ता सतᭅकता बीकानेर के िनदᱷशानुसार आज ᳰदनांक \n1.4.17  को पीएम गजनेर पᱟंचे तो मौके पर थाना पᳯरसर मᱶ एक वाहन सं᭎या RJ07GB9307 िजसमᱶ थाना पर ᮧ᭭तुत \nकᳱ गई कांटा पचᱮ अनुसार 28 टन खिनज िज᭡सम से भरा खङा है थाने मᱶ उपि᭭थत वाहन चालक से पूछताछ करने पर \nउसने अपना नाम ल᭯मण पुᮢ ई᳡रराम जाित िब᳤ोई िनवासी रामपुरा ब᭭ती गली . 20 को होना बताया। वाहन चालक से \nखिनज िज᭡सम के वैध कागजात रव᳖ा /रॉय᭨टी रसीद होने से मना कर ᳰदया एवं बताया ᳰक वह उᲦ खिनज िज᭡सम िबना \nरव᳖ा ,रॉय᭨टी रसीद के अवैध ᱧप से चोरी छुपे कायमवाला से भरकर लाया है थाना पᳯरसर मᱶ मौका पंचनामा बनाकर \nवाहन चालक को िनयमानुसार पेन᭨टी रािश जमा कराने को कहा तो उ᭠होने असमथᭅता ᳞Ღ कᳱ अतः वाहन को मय खिनज \nज᭣त सरकार करते ᱟए पीएस गजनेर  कᳱ सुपुदᭅगी मᱶ ᳰदया गया। वाहन चालक /मािलक का उᲦ कृ᭜य MMDR ACT \n1957 कᳱ धारा 4/21,  RMMCR2017 के िनयम 54 व 60, IPC कᳱ धारा 379  के तहत द᭛डनीय अपराध है। अतः \n᮰ीमान जी से िनवेदन है ᳰक वाहन चालक/मािलक के िवᱧ᳍ मुकदमा दजᭅ कर कठोर कानूनी कायᭅवाही कराने का ᮰म करावे। \nसंलᲨ –मूल मौका पंचनामा भवदीय एस.डी.ह.तीथᭅराज एमएफ 2खिनज िवभाग कोलायत,बीकानेर ,पेश कᳱ। िजस पर \nअिभयोग सं᭎या 30/2017 धारा 379 भादस , 4,21एमएमडीआर ए᭍ट  मᱶ दजᭅ कर त᭢तीश सुपुदᭅ ᮰ी गोकुलराम हैड \nकािन.04 के कᳱ गयी। एफआईआर ᮧितयां िनयमानुसार जारी कᳱ गयी। \nDirected (Name of I.O.):\n(जाँच अिधकारी का नाम ):ᮧधान िसपाहीRank \n(पद):\n to take up the Investigation (को जाँच अपने पास मᱶ लेने के िलए िनदᱷश ᳰदया गया) or(या)(2)Since the above information reveals commission of offence(s) u/s as mentioned at Item No. 2.\n(1)\n(3)13.\n Refused investigation due to \n (जाँच के िलए) :      Gokul  Ram\nNo(सं.):Registered the case and took up the investigation (ᮧकरण दजᭅ ᳰकया गया और जाँच के िलए िलया गया):Action taken :\n04 or (या)(कᳱ गई कायᭅवाही: चूँᳰक उपरोᲦ जानकारी से पता चलता हᱹ ᳰक अपराध करने का तरीका मद सं.2 मᱶ उ᭨लेख धारा के तहत हᱹ):\n or (के कारण इंकार ᳰकया, या)\nTransferred to P.S.(थाना): District (िजला): (4)\non point of jurisdiction (को ᭃेᮢािधकार के कारण ह᭭तांतᳯरत) .\nF.I.R.read over to the complainant/informant,admitted to be correctly recorded and a copy given to the\ncomplainant/informant free of cost.\nR.O.A.C.(आर.ओ.ए.सी.)(िशकायतकताᭅ / सूचनाकताᭅ को ᮧाथिमकᳱ पढ़ कर सुनाई गई, सही दजᭅ ᱟई माना और एक ᮧित िनःशु᭨क िशकायतकताᭅ को दी गई|)12.First Information contents (Attach separate sheet, if necessary)\n (ᮧथम सूचना त᭝य(यᳰद आव᭫यक हो , तो अलग पृ᳧ न᭜थी करे)):S.No. \n(ᮓ.सं.)UIDB Number \n(यू.आई.डी.बी. सं᭎या)\n3N.C.R.B/एन.सी.आर.बी\nI.I.F.-I /एकᳱकृत जाँच फामᭅ-I\n14.\n15.Signature/Thumb impression of the complainant / informant \n(िशकायतकताᭅ / सूचनाकताᭅ के ह᭭ताᭃर / अंगूठे का िनशान):\nDate and time of dispatch to the court\n(अदालत मᱶ ᮧेषण कᳱ ᳰदनांक और समय):SI (Sub-Inspector)Inder  Kumar Name(नाम):\nRank (पद):\nNo(सं.): \nSignature of Officer in charge, Police Station\n(थाना ᮧभारी के ह᭭ताᭃर)\nERUTANGIS00X ERUTANGIS00Y\n4N.C.R.B/एन.सी.आर.बी\nI.I.F.-I /एकᳱकृत जाँच फामᭅ-I\nAttachment to item 7 of First Information Report (ᮧथम सूचना ᳯरपोटᭅ के मद 7 संलᲨक):\nPhysical features, deformities and other details of the suspect/accused:(If known/seen )\n(संᳰद᭏ध / अिभयुᲦ कᳱ शारीᳯरक िवशेषताएँ, िवकृितयाँ और अ᭠य िववरण :(यᳰद ᭄ात / देखा गया))\n1987 1 पुᱧषS.No.(ᮓ.सं.) Sex (ᳲलग) Date/Year of Birth \n( ज᭠म ितिथ / वषᭅ)Build \n(बनावट)Height(cms.)\n(कद(से.मी))Identification Mark(s)\n(पहचान िच᭠ह)Complexion (रंग )\n1 2 3 4 5 7 6\nDeformities/ Peculiarities  \n(िवकृितयाँ/ िविश᳥ताएँ)Teeth\n(दाँत)Hair\n(बाल)Eyes\n(आँखᱶ)Habit(s)\n(आदतᱶ)Dress Habit(s)\n(पहनावा)\n8 9 10 11 12 13\nPlace Of(का ᭭थान) Language /Dialect \n(भाषा /बोली)Burn Mark \n(जले ᱟए का \nिनशान) Mole\n(म᭭सा)Leucoderma\n(धवल रोग )Scar\n(घाव)Tattoo\n(गूदे ᱟए का)Others \n(अ᭠य) \n14 15 17 16 18 19 20\nThese fields will be entered only if complainant/informant gives any one or more particulars about the suspect/accused.\n(यह ᭃेᮢ तभी दजᭅ ᳰकए जाएंगे यᳰद िशकायतकताᭅ / सूचनाकताᭅ संᳰद᭏ध / अिभयुᲦ के बारे मᱶ कोई एक या उससे अिधक जानकारी देता है |)\n5"
   }

  ```

  or

  ![img-3](https://github.com/Devparihar5/RJPOLICE_HACK_668_NeuralNomards_4/blob/test/demo-images/ocr-demo/demo.png)
