# Darba_slud
Darba sludinājumu atlasīšana

Darba uzdevums:
      Projekta uzdevums ir vienkāršot darba sludinājumu meklēšanas procesu. Personīgi man daudz laika tiek patērēts atverot mājaslapu, aizverot sīkdatnes un reklāmas, atzīmējot, tos pašus kritērijus tikai, lai neieraudzītu nevienu jaunu sludinājumu. Tāpēc es nolēmu paātrināt šo procesu.   
    Paša projekta būtība ir pātrtraukt pārlūkprogrammas darbību, ja nav
neviena jauna darba piedāvājuma, turpretī, ja ir, tad atstāt to atvērtu un ļaut man paskatīties jauno sludinājumu. Kā arī visas profesijas, kas tiek piedāvātas, to nosaukumi tiek nolasīti un pievienoti teksta failam. Protams, ja tie jau tur nebija iepriekš. Tas ir ar mērķi, lai noskaidrotu kādi darba piedāvājumi manos atzīmētos kritērijos eksistē.

Izmantotās bibliotēkas:

  Selenium: tiek izmantots, lai automatizētu pārlūkprogrammas darbību un darbības mājaslapā. Tas ir pamats manai programmai, jo ar Selenium palīdzību tiek: atvērta mājaslapa, driver.get(url). Gaidīšana kamēr tā atveras(WebdriverWait). Aizvērta reklāma kā arī atlasīti kritēriji ar find_element() un click(). Driver.refresh(), lai atjauninātu url un saturu.

  bs4: šī bibliotēka tiek izmantota, lai veiktu darbības ar HTML struktūru no mājaslapas jeb tīmekļa skrāpēšanu. Ar šīs bibliotēkas palīdzību tika izgūti profesiju nosaukumi no tīmekļa vietnes. Meklējot elementus pēc to atribūtiem, HTML struktūrā. Tika meklēti elementi pēc span, ID, vai klases.

Galvenās metodes:

  Galvenās metodes šajā projektā bija find_element(By…) un click(). Tas palīdzēja atrast vajadzīgos elementus pēc klases vai id un imitēt peles klikšķi. Nēmot vērā Inspect rīku, tīmekļa vietnē varēja nolasīt mājaslapas struktūru un katra elementa atribūtu.
  Otrajā programmas daļā, kur tika izmantota BeautifulSoup bibliotēka galvenā metode bija html.parser, kas ļāva metodei find_all() atrast visus elementus ar nepieciešamo klasi. Beigās tika izmantotas metodes, kas tika mācītas semestra sākuma par teksta failu apstrādi. “a” lai papildinātu failu, “r” lai nolasītu failu. Write() un read(), lai rakstītu failā un nolasītu tā saturu.

