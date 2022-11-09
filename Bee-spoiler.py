## load file with words
## Source of list https://www-personal.umich.edu/~jlawler/wordlist.html

# set up working directory to source file location before running script

def load_words():
    with open('wordlist3.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
  

word_list = load_words()


def bee_spoiler(word_list, central_letter, peripheral_letters):
  '''Solves the Spelling Bee of the New York times by creating a list of words that comply with the rules:'''
  '''Words must only include the provided letters. The central one is mandatory'''
  '''Words must be at least 4-letters long'''
  
  #word_list = load_words()
  
  bees = [] #initialize results list
  
  pangram =[]
  
  
  letters = set(peripheral_letters) # create a set with the peripheral letters
  
  letters.add(central_letter) # add central letter to set. 
  
  for word in word_list:
    
    #word.lower() # convert to lowercase (or whatever case the word list is)
    
    word_letters = set(word) # creates a set with the letters in word
    
    if len(word) < 4 or central_letter not in word_letters: # words must be at least 4-letter long and include the central letter
      continue
    
    elif word_letters == letters:
      pangram.append(word)
    
    
    elif word_letters.issubset(letters):
      bees.append(word)
    
  print('Today I found ' + str(len(bees)) + ' words and ' + str(len(pangram)) + ' pangram/s')
  print(*sorted(bees), sep = ', ')
  print('Pangram/s:')
  print(*pangram)
 
  
  
  #return sorted(bees), pangram
  

 
# add missing words from NYT

new_words = ('baaing', 'bailing', 'baling', 'balling', 'bianual', 'binging', 'binning', 'blabbing', 'bling', 'bubba', 'bugging', 'bugling', 'gabbing', 'gabbling', 'gibing', 'labia', 'lubing', 'nabbing', 
'nibbling', 'nubbin', 'unbag', 'unbagging', 'unban', 'unbanning','dunno', 'udon', 'twilit', 'wanna', 'facticity', 'citify', 'fillialy', 'glug', 'halal', 'luau', 'lulu', 'banc', 'captcha', 'catchup', 
'hatha', 'huzzah', 'tach', 'capellini' 'enlace', 'cannellini', 'finito', 'mentee', 'demit', 'demitted', 'airboat', 'arborio', 'barrio', 'aptly', 'eely', 'lethally', 'papally', 'pappy', 'patly', 'phyla', 
'tatty', 'teleplay', 'teletype', 'yappy', 'deeded', 'hied', 'teed', 'teethed', 'tithed', 'acidy', 'caiman', 'canid', 'indica', 'indicia', 'minicam', 'minyan', 'alit', 'optimmal', 'focaccia', 'falloff',
'optima', 'taillamp', 'tali', 'tallit', 'tatami', 'gimme', 'hemmming', 'hitmen', 'meming', 'minting', 'emcee', 'emceed', 'enchain', 'heinie', 'innie', 'annularly', 'aunty', 'aura', 'aurally', 'lull', 
'runny', 'runty', 'rural', 'rurally', 'rutty', 'tautly', 'truly', 'tutu', 'ultra', 'yurt', 'taut', 'journo', 'runaround', 'canna', 'enlace', 'naan', 'pogo', 'ogee', 'ammo', 'foci', 'coact', 'annal', 
'koan', 'mammon', 'admin','acceded', 'caged', 'canceled', 'candela', 'caned', 'ceded', 'celled', 'danced', 'enlaced', 'glace', 'lanced', 'dino', 'indicia', 'decked', 'dink', 'iffy', 'folic', 'dinked',
'inked', 'kicked', 'nicked', 'kidded', 'kinked', 'pecked', 'peeked', 'picknicked', 'pinked', 'deke', 'deked', 'eked', 'kenned', 'kiddie', 'peke', 'bronzing', 'booing', 'aloofly', 'calcify', 'noob',
'bogging', 'boozing', 'binning', 'boning', 'ribboning', 'boing', 'brinning', 'bonobo', 'bribing', 'robing', 'italicize', 'celli', 'electee', 'latte', 'laze', 'tacet', 'moppet', 'onetime', 'demonize', 
'demonized', 'died', 'dimmed', 'dined', 'dizzied', 'doozie', 'eddied', 'indie', 'iodized', 'mimed', 'mimeo', 'pepita', 'pipet', 'vape', 'veep', 'draping', 'parading', 'dapping', 'dinar', 'dinging', 
'girding', 'grandad', 'grandpapa', 'panda', 'priding', 'radii', 'raiding', 'ridging', 'javelina', 'eave', 'liven', 'nene', 'villanelle', 'lave', 'competed', 'coded', 'coed', 'comp', 'comped', 'cooed', 
'cooped', 'coopt', 'coped', 'coped', 'copped', 'deco', 'decode', 'decoded', 'detected', 'dotcom', 'coopted', 'decoct', 'decocted', 'heeded', 'hewed', 'hoed', 'hoedown', 'honed', 'hooey', 'howdy', 'nohow', 
'whee', 'woohoo', 'yoohoo', 'onto', 'topcoat', 'tempeh',  'empath', 'pampa', 'pate', 'phat', 'teepee', 'affirming', 'frag', 'fragging', 'framing', 'fringing', 'infirming', 'infringing', 'miffing','riffing', 
'faring', 'farming', 'fifing', 'fining', 'naif', 'midtown', 'tomtit', 'mondo', 'techie', 'tiki', 'kente', 'uncool', 'colleen', 'neocon', 'noel', 'oleo', 'donut', 'outro', 'runout', 'romcom', 'camo', 
'availed', 'aviated', 'deviated', 'deviled', 'dived', 'divvied','laved', 'titivated', 'valeted', 'vetted', 'levitated', 'validate', 'dative', 'delved', 'evaded', 'leveled', 'levied', 'levitate', 'vied', 
'itty', 'droid', 'cocci', 'hailed', 'healed', 'heeled', 'hilled', 'deadheaded', 'helipad', 'phalli', 'grumping', 'grinning', 'gripping', 'inuring', 'inurning', 'mirin', 'miring', 'nigiri', 'purring', 
'ripping', 'ruing', 'ruining', 'umpiring', 'unrigging', 'purging', 'rigging', 'rimming', 'eyetooth', 'honeypot', 'hooey', 'hoppy', 'hotpot', 'phono', 'pone', 'tonne', 'toon', 'typo', 'nonet', 'peyote', 
'algae', 'gelee', 'henge',  'nonagonal', 'google', 'lowdown', 'wildwood', 'evened', 'ovine', 'vended', 'vetoed', 'voided', 'voted', 'envied', 'devein', 'deveined', 'divined', 'invitee', 'videoed', 'citing',
'exiting', 'igniting', 'inciting', 'nite', 'tenting', 'texting', 'tinging', 'teeing','tingeing', 'kilo', 'acai', 'cacti', 'tailcoat', 'tikka', 'toolkit', 'cyan', 'ancho', 'honcho', 'anyhoo', 'giggled',
'highlighted', 'lighted', 'eggged', 'gigged', 'gilled', 'glided', 'legit', 'lighted', 'gelded', 'gelled', 'cootie', 'ecotone', 'toughen', 'gotten', 'outgun', 'outthought', 'outgone', 'unhung', 'unthought',
'tidally', 'daylit', 'daylily', 'gowning', 'lowing', 'owning', 'wiggling', 'winging', 'winnowing', 'wino', 'wowing', 'bathmat', 'mambo', 'momma', 'marm', 'haram', 'mahatma', 'mammoth', 'affiliate', 'fella', 
'fellate', 'feta', 'filet', 'leftie', 'facelift', 'nada', 'nana', 'natant', 'garbanzo', 'boba', 'toro', 'tori', 'torii', 'rotini', 'attacked', 'cackled', 'caked', 'clacked', 'keeled', 'lacked', 'leaked',
'tacked', 'tackled', 'latke', 'majorly', 'moola', 'moll', 'amorally', 'ably', 'anally', 'ballboy', 'banally', 'blabby', 'blobby', 'cabby', 'looony', 'onlay', 'chinning', 'chucking', 'chugging', 'cinching', 
'ginning', 'gunning', 'hinging', 'hugging', 'hunching', 'inching', 'inking', 'kinging', 'kinking', 'nicking', 'nuking', 'unhinging', 'unhung', 'unkink', 'unkinking', 'chunking', 'zine', 'hiking', 'hinging', 
'cuing', 'nunchuck', 'nunchuk', 'initialize', 'netizen', 'trod', 'cardio', 'peen', 'unpeg', 'unpen', 'punny', 'corrida', 'didact', 'octad', 'mooching', 'mooch', 'cocooning', 'coining', 'gnocchi', 'mochi', 
'oncoming', 'conning', 'noncom', 'drib', 'moron', 'pram', 'promo', 'ached', 'aided', 'cached', 'hacked', 'caddied', 'chia', 'chai', 'chica', 'haka', 'ahoy', 'achoo', 'aplenty', 'patently', 'latently',
'palely', 'penally', 'netty', 'panty', 'leanly', 'yente', 'hinting', 'hitching', 'nitwit', 'thinning', 'twinging', 'twinning', 'twitching', 'farro', 'fora', 'froufrou', 'chalked', 'heckled', 'leached', 
'leeched', 'lech', 'cirri', 'citric', 'nitro', 'nori', 'croc', 'croci', 'toric', 'tortoni', 'auguring', 'linguini', 'lunging', 'lulling', 'unilingual', 'iguana', 'annuli', 'annuling', 'lulling', 'luring',
'arugula', 'glugging', 'gluing', 'gulling','gurgling', 'lugging', 'took', 'woot', 'whammo', 'gazillion', 'glazing', 'ionizing', 'lazing', 'lionizing', 'oozing', 'zigging', 'zagging', 'couched', 'douched',
'duded', 'duetted', 'educed', 'etude', 'educed', 'hued', 'outed', 'thudded', 'touche', 'touted', 'tutted', 'befell', 'flatbed', 'beefed', 'deflate', 'leafed', 'fellated', 'defat', 'defatted', 'deadfall',
'flatfeet', 'cami', 'manic', 'minty', 'appellee', 'palapa', 'palp', 'conceived', 'connived', 'convened', 'convinced', 'inconvenienced', 'invoiced', 'Cyclically', 'malic', 'coca', 'callaloo', 'pinup', 'unpin',
'puli', 'meze', 'mezee', 'titmice', 'concocting', 'condo', 'condoning', 'connoting', 'cottoning', 'indicting', 'noticing', 'dicing', 'offload', 'coinciding', 'boffo', 'blithely', 'lithely', 'yeti' ,
'photomap', 'bloomed', 'boomed', 'bombed', 'deemed', 'demo', 'demoed', 'domed', 'emend', 'loomed', 'meddled', 'melded', 'mended', 'mooned', 'mobbed', 'noblemen', 'bellmen', 'melodeon', 'mooed', 'memed',
'chocoholic', 'catchall', 'litho', 'mezze', 'bazoo', 'tamari', 'primal', 'vacated', 'vaxxed', 'vaxed', 'taxa', 'tatted', 'excavated', 'aced', 'axed', 'caved', 'exacted', 'taxed', 'hourlong', 'logroll',
'bloop')

word_list.update(new_words)

# remove words not accepted by NYT

remove_words = ('a-horizon', 'a-ok', 'aardvark', 'aardwolf', 'ab', 'aba',  'alauda', 'aleut', 'alula', 'aude', 'auld', 'deau', 'defluat', 'elul', 'etude', 'fauld', 'faule', 'faut', 'faute',
'fula',  'fullfed', 'leau', 'llud', 'luff', 'luffa', 'lulld', 'tulle', 'tulu', 'tuta', 'ullalulla', 'alaw', 'illwill', 'nwill', 'taiwan', 'wadi', 'wain', 'witan', 'caff', 'caitiff', 
'calcific', 'cfallacy', 'facit', 'facta', 'facti', 'fait', 'fata', 'fatta', 'fica', 'taft', 'aevi', 'alvine', 'avellan', 'avena', 'avile', 'bavin', 'bivalvia', 'eleve', 'enviva', 'ecce', 
'cela', 'canellaceae', 'nacelle', 'eveille', 'leve', 'levin', 'neve', 'vali', 'vana', 'veinal', 'vena', 'veni', 'veniable', 'vennel', 'vielle', 'enki', 'kike', 'kidd', 'pipkin',
'vienna', 'viii', 'vila', 'villein', 'villi', 'villian', 'vina', 'viva', 'vive', 'vlei', 'akan', 'alla', 'allo', 'amman', 'annona', 'anoa', 'anomala', 'kaka', 'kala', 'kalon', 'kama', 'kann', 'kaon',
'kawaka', 'klan', 'kokka', 'kolam', 'kwannon', 'maana', 'makomamko', 'mala', 'malmo', 'mamo', 'manama', 'manannan', 'mann', 'biggin', 'birr', 'gobi', 'gobio', 'bonn', 'bono', 'bing', 'cito',
'clinton', 'coction', 'coition', 'colton', 'conto', 'cotillon', 'inconcoction', 'init', 'initio', 'inti', 'lomotil', 'loti', 'milt', 'milton', 'molto', 'ticino', 'timon', 'titi', 'nonmonotonic', 'nont',
'acatalectic', 'aceite', 'actaea', 'aecial', 'aile', 'alate', 'alcea', 'alea', 'alee', 'allelic', 'alliaceae', 'attalea', 'aztec', 'cactaceae', 'caeca', 'caecal', 'catalectic', 'cecal', 'celt', 'cetacea',
'ciel', 'ciliate', 'clitellae', 'eile', 'elli', 'etat', 'illae', 'lactea', 'laelia', 'latet', 'leal', 'leti', 'licet', 'liliaceae', 'taccaceae', 'tace', 'tael', 'tecta', 'tete', 'tetee', 'tiliaceae',
'tilletia', 'tilletiaceae', 'tittletattle', 'zetetic', 'emmet', 'empo', 'enim', 'mein', 'mene', 'menippe', 'menomini', 'menopon', 'mente', 'zion', 'zooid', 'ondine', 'omni', 'odin', 'nonionized', 'nomine',
'momemt', 'mommon', 'monition', 'mont', 'montee', 'motet', 'motmot', 'motte', 'neem', 'neminem', 'nemo', 'omne', 'pompeii', 'pompon', 'demi', 'minden', 'dido', 'diodon', 'dioon', 'domi', 'dizen',
'domini', 'dominie', 'endenizen', 'imide', 'indene', 'medio', 'meiden', 'midden', 'minden', 'nemine', 'pontem', 'temnit', 'tempete', 'timeo', 'timon', 'toimeme', 'tompion', 'tomtom', 'mentem', 'onine',
'capacitive', 'acceptive', 'accepta', 'apatite', 'apia', 'apie', 'apte', 'capapie', 'capit', 'capitate', 'capite', 'capiti', 'epact', 'icecap', 'iiip', 'paca', 'papeete', 'pataca', 'peccavi', 'pectic',
'peice', 'picea', 'piet', 'pieta', 'piete', 'pitta', 'taipei', 'tappet', 'tipcat', 'pipa', 'adad', 'adaga', 'adapa', 'adapid', 'adar', 'andira', 'adapana', 'argand', 'facia', 'falco', 'focally', 'illoff', 
'dada', 'dagan', 'dagda', 'dagga', 'danaid', 'dandi', 'dandin', 'dard', 'diana', 'gaddi', 'giardia', 'gidar', 'granada', 'india', 'indian', 'indianan', 'inding', 'indra', 'nard', 'niggard', 'locofoco', 'officio',
'padda', 'pandar', 'ajee', 'alanine', 'aliene', 'alieni', 'anele', 'anile', 'aniline', 'elaine', 'enlil', 'jena', 'lena', 'lenin', 'linea', 'linnaea', 'nella', 'nenia', 'nile', 'valine', 'cocotte', 'codem',
'comme', 'compt', 'compte', 'copepod', 'copt', 'decet', 'docet', 'ecco', 'ecto', 'medoc', 'poco', 'compo', 'dhow', 'heydey', 'hoddydoddy', 'hoyden', 'ohne', 'yodh', 'yoho', 'annatto', 'anno', 'annotto', 'atto',
'cato', 'cocopa', 'conatu', 'connu', 'coon', 'cotta', 'cout', 'noctua', 'nona', 'nota', 'otto', 'panto', 'pcoat', 'poca', 'ponca', 'poon', 'potto', 'potu', 'puccoon', 'puncto', 'tanoan', 'tanto', 'tauon', 
'toona', 'toto', 'cuon', 'puto', 'ephah', 'hypha', 'mayhap', 'ptah', 'typha', 'anfang', 'fagging', 'fagin', 'fain', 'fama', 'fing', 'finn', 'firma', 'firman', 'firmiana', 'fari', 'fragaria', 'frangi', 'frigg',
'giraffa', 'infra', 'niff', 'raff', 'fairing', 'dinmont', 'modo', 'monodon', 'ctene', 'enceinte', 'entete', 'heth', 'hitchiti', 'hittite', 'kent', 'nicht', 'niente', 'tehee', 'tektite', 'tench', 'tente', 'teth', 
'tien', 'tiene', 'tike', 'tinnient', 'coll', 'eocene', 'felloe', 'felo', 'feoff', 'feoffee', 'floccule', 'foule', 'leone', 'leuco', 'lolo', 'nolle', 'confluenee', 'coelo', 'acned', 'cada', 'adde', 'aden', 'andean',
'cade', 'cadenced', 'cadj', 'canada', 'cycad', 'cycadaceae', 'dacca', 'danae', 'danaea', 'edda', 'eden', 'yade', 'abrocoma', 'acroama', 'ambo', 'amor', 'arma', 'bamako', 'barmbrack', 'brama', 'cabomba', 'camorra', 
'carrom', 'coram', 'crambo', 'kamba', 'karakoram', 'macaca', 'makomako', 'mara', 'maraco', 'marc', 'marcor', 'markka', 'marmara', 'moorcock', 'mora', 'morbo', 'barm', 'mormo', 'morra', 'rama', 'roma', 'adnoun', 'anuran',
'aoudad', 'arundo', 'aruru', 'aurar', 'auro', 'auroroa', 'danu', 'datura', 'dura', 'durra', 'nantua', 'narratur', 'natura', 'nauran', 'nauru', 'nauruan', 'nuda', 'orotund', 'ruat', 'rudd', 'rudra', 'ruta', 'tautara', 
'tudor', 'turd', 'tutto', 'utra', 'urdu', 'alleviative', 'avadavat', 'daeva', 'davallia', 'david', 'davit', 'deev', 'deva', 'devel', 'devi', 'illative', 'latvia', 'levite', 'titillative', 'vade', 'vail', 'valde',
'valeat', 'valletta', 'valved', 'veda', 'vedalia', 'vedette', 'vedi', 'velit', 'velveeta', 'vida', 'vide', 'viddi', 'vita', 'vitae', 'vitia', 'vivit', 'daeva', 'davallia', 'david', 'davit', 'deev', 'devel', 'devi', 
'titillative', 'vade', 'valde', 'valeat', 'valete', 'valletta', 'valved', 'veda', 'vedalia', 'vedette', 'vedi', 'velit', 'velveeta', 'vida', 'vidi', 'hight', 'alar', 'alliaria', 'andorra', 'andorran', 'arado', 'aralia', 
'arno', 'drindl', 'aroid', 'dari', 'donar', 'dorian', 'droil', 'indri', 'iran', 'irani', 'iranian', 'iroin', 'laird', 'lari', 'linaria', 'lora', 'lorn', 'naira', 'nidor', 'nord', 'noria', 'norn', 'nornal', 'ollari', 'onor',
'orad', 'oran', 'ordinand', 'ordo', 'orion', 'orlando', 'orlon', 'radiolaria', 'randan', 'rara', 'rarior', 'raro', 'rodolia', 'roland', 'ronian', 'rorid', 'radiolarian', 'larid', 'loir', 'nardoo', 'narial', 'rana', 
'rari', 'roral', 'comminution', 'comon', 'conium', 'coucicouci', 'cuminum','cunnint', 'cunt', 'ictu', 'inimicum', 'inunction', 'micomicon', 'mucin', 'nonionic', 'monocot', 'nunc', 'nuncio', 'ocimum', 'omotic', 'timucu',
'addlehead','allah', 'aphididae', 'delilah', 'delphi', 'dphil', 'elaphe', 'ephippidae', 'hadal', 'haha', 'haida', 'haldea', 'halide', 'hallel', 'heald', 'heddle', 'hipped', 'philip', 'philippi', 'didelphidae',
'philadelphia', 'delhi', 'heil', 'girru', 'grig', 'grig', 'grigri', 'grimm', 'grugru', 'grum', 'gunrunning', 'mimir', 'miri', 'primum', 'purim', 'rimu', 'uigur', 'unmurmuring', 'epopee', 'eyot', 'honte', 'hoopoe',
'hoth', 'hottentot', 'nonny', 'opepe', 'pennon', 'peptone', 'petto', 'phon', 'phot', 'poohpooh', 'poohpoohpooh', 'poteen', 'tenon', 'tetto', 'thoth', 'toetoe', 'tophet', 'toyon', 'typhon', 'tyto', 'aegean', 'aghan',
'agonal', 'algol', 'anagoge', 'angola', 'angolan', 'eloge', 'enallage', 'gaea', 'gael', 'galago', 'galan', 'galega', 'galen', 'galena', 'gaol', 'gean', 'gehenna', 'genoa', 'ghana', 'gheg', 'glenn', 'glogg', 
'gogo', 'hegel', 'hellhag', 'lagan', 'lang', 'legon', 'llaga', 'logan', 'loggan', 'longo', 'naga', 'nonage', 'diol', 'lido', 'lilo', 'linn', 'lowlihood', 'lown', 'nihil', 'nihilo', 'nill', 'noli', 'olid', 'wold', 'london', 
'devon', 'divino', 'eventide', 'evove', 'invenit', 'invente', 'invito', 'novo', 'ovid', 'totitive', 'vendee', 'veneto', 'veniente', 'venit', 'vident', 'vient', 'vino', 'vivendi', 'voivode', 'voto', 'indevotion', 'dinvention',
'cigit', 'eget', 'entgtg', 'exegetic', 'genet', 'gete', 'gite', 'ingenite', 'tetigit', 'ting', 'tingent', 'tinning', 'acti', 'alalia', 'alcaic', 'alia', 'altaic', 'attica', 'attila', 'cacalia', 'calcic', 'calcitic', 'catalitic',
'ciliata', 'coattail', 'collocalia', 'illa', 'kali', 'kalki', 'kiack', 'kila', 'killick', 'kitcat', 'lait', 'latitat', 'loki', 'ocotillo', 'otia', 'otic', 'talia', 'ticktack', 'tilia', 'alkalotic', 'catalatic', 'clio', 'kaki',
'anna', 'aphony', 'ayapana', 'chon', 'concha', 'conoy', 'nanna', 'napha', 'nappy', 'noah', 'ochna', 'yana', 'yanan', 'dight', 'dighted', 'ghillie', 'gidgee', 'gillie', 'giltedged', 'gleet', 'goethe', 'goutte', 'guenon', 'guet',
'higgle', 'higi', 'igigi', 'tedge', 'lightlegged', 'cento', 'concetto', 'conte', 'coontie', 'icenot', 'inconnection', 'necio', 'nicene', 'nocet', 'noncontent', 'euge', 'genou', 'gentoo', 'genug', 'gungho', 'hugo', 'nung', 
'ough', 'thuggee', 'tongu', 'ungue', 'huguenot', 'togo', 'hough', 'adalia', 'adit', 'aditi', 'aditya', 'alid', 'dalal', 'davy', 'dita', 'iliad', 'italy', 'lally', 'layia', 'tala', 'yalta', 'allyl', 'alta', 'golliwog', 'wilig', 'woon',
'abohm', 'abraham', 'amah', 'amhara', 'amort', 'amoto', 'brahm', 'brahma', 'homo', 'mahabharata', 'marah', 'maratha', 'marmota', 'mort', 'omaha', 'rhomb', 'tamtam', 'morta', 'elief', 'facetiae', 'facie', 'faille', 'falcate',
'fece', 'fecit', 'felice', 'felicia', 'fictile', 'fieff', 'fille', 'flatlet', 'flecti', 'leef', 'lief', 'teff', 'felicitate', 'anodonta', 'dado', 'doha', 'dona', 'donna', 'haud', 'haut', 'nata', 'oahu', 'odonata', 'othonna',
'tant', 'thana', 'toda', 'utah', 'utahan', 'abba', 'abra', 'arab', 'araba', 'araroba', 'arroba', 'babar', 'barba', 'barong', 'boann', 'bona', 'borago', 'bragg', 'gabbro', 'gabon', 'roba', 'bara', 'fitout', 'forint', 'forti', 'fortior',
'fortiori', 'fount', 'fronti', 'furto', 'futuri', 'intort', 'intout', 'itur', 'nintu', 'nitor', 'nuit', 'oritur', 'orti', 'tiffin', 'toff', 'toronto', 'torr', 'tor', 'futurition', 'introit', 'trottoir', 'trunnion', 'ackee', 'akee',
'deckled', 'taka', 'takk', 'tekel', 'calk', 'keck', 'alamo', 'alma', 'llyr', 'lolly', 'loma', 'lory', 'lyra', 'lyram', 'malay', 'malayalam', 'malm', 'malo', 'marl', 'mylar', 'olmo', 'orly', 'accloy', 'accoy', 'albany', 'babylon', 
'baya', 'blolly', 'booly', 'coyol', 'layby', 'looby', 'lyon', 'nyala', 'yacca', 'cooly', 'bobby', 'chink', 'chinking', 'cucking', 'gink', 'hinc', 'hunc', 'nguni', 'ninigi', 'chungking', 'anil', 'anni', 'attaint', 'inani', 'inanna', 
'intelleet', 'italian', 'laniate', 'latin', 'latinate', 'liana', 'liza', 'naiant', 'natantia', 'nati', 'nina', 'nitella', 'taenia', 'taeniate', 'tallinn', 'tantalilte', 'tanti', 'tantilla', 'tanzania', 'tanzanian', 'tinea', 
'titian', 'zinnia', 'zill', 'zizania', 'acadia', 'acarid', 'acidotic', 'adriatic', 'arcadic', 'arctiid', 'caddo', 'cadi', 'cadit', 'cadra', 'cardia', 'coaid', 'coccoid', 'corda', 'cordia', 'dacoit', 'dicot', 'dicto', 'dirca', 'doit',
'doodia', 'doric', 'dort', 'draco', 'droit', 'iridic', 'ricordo', 'ridotto', 'tadarida', 'tardi', 'tortricid', 'todo', 'trad', 'acardia', 'punce', 'pung', 'chinch', 'choc', 'cochimi', 'cochin', 'coign', 'congo', 'gnomic', 'inchon',
'mich', 'ohmic', 'abiit', 'adhibit', 'ahab', 'arabia', 'arariba', 'bari', 'bata', 'batta', 'bihar', 'bihari', 'bitt', 'briard', 'brit', 'daba', 'dabri', 'draba', 'rabat', 'ratibida', 'tabi', 'tabid', 'tabita', 'tibi', 'titbid', 'lamna',
'monal', 'mormon', 'nonmoral', 'norma', 'norman', 'oman', 'pallmall', 'palmam', 'palmar', 'pomo', 'praam', 'ramman', 'roman', 'romana', 'romanal', 'romona', 'cachi', 'cicadidae', 'dhak', 'hacek', 'hackee', 'haec', 'haik', 'hakka', 'hecha',
'kachcha', 'kadai', 'kadi', 'keddah', 'kichai', 'navaho', 'hoya', 'leyte', 'paye', 'payena', 'pennya', 'pennyante', 'platy', 'playa', 'tenpenny', 'tyne', 'yean', 'twitting', 'aframomum', 'arulo', 'faro', 'fomor', 'foram', 'forma', 'foro',
'fumo', 'ormolu', 'caleche', 'chachalaca', 'chela', 'hakea', 'khalkha', 'cheeked', 'corno', 'croton', 'nfor', 'octoroon', 'octroi', 'orinoco', 'rocroi', 'roric', 'corto', 'croft', 'agua', 'agural', 'agurial', 'alular', 'anguill', 
'anguilla', 'anguillan', 'anguillula', 'auri', 'auriga', 'gallinula', 'gauguin', 'gaul', 'gauri', 'guan', 'guarani', 'guiana', 'gula', 'iglu', 'inula', 'langur', 'ligularia', 'liguria','lunaria', 'lungi', 'lunular', 'nulli',
'ungual', 'urania', 'uria', 'urial', 'unalluring', 'gaur', 'lingual', 'inulin', 'irula', 'lingua', 'nulla', 'kota', 'koto', 'kotoko', 'kotow', 'ottawa', 'tokamak', 'hawkmoth', 'azolla', 'azonal', 'gazania', 'giza', 'izanagi', 'nazi',
'zingano', 'zola', 'chut', 'cohue', 'couchette', 'coute', 'cutch', 'dutch', 'eheu', 'touchd', 'toute', 'duce', 'abaft', 'befated', 'dafe', 'deffle', 'delf', 'faddle', 'fatted', 'felted', 'amain', 'amanita', 'amia', 'amici', 'amicitia',
'animam', 'animi', 'cyma', 'immanity', 'intima', 'mammy', 'matai', 'matin', 'maya', 'mayaca', 'mayan', 'miami', 'micmac', 'tammany', 'tammy', 'tiamat', 'yama', 'antimycin', 'minacity', 'alca', 'apella', 'appal', 'capella', 'clepe', 'jacal',
'lapp', 'palce', 'pellaea', 'plap', 'coceive', 'covin', 'dciived','divoce', 'venice', 'vici', 'vindice', 'vedic', 'acomia', 'allylic', 'amical', 'calamo', 'camail', 'camilla', 'clammily', 'coccal', 'colima', 'comica', 'cycloloma', 'loca',
'macao', 'malacca', 'malacia', 'malcolmia', 'mccoy', 'alpinia', 'lapful', 'lapin', 'napu', 'nipa', 'pani', 'papain', 'papuan', 'papula', 'paul', 'pili', 'pinna', 'pipal', 'pula', 'upupa', 'metic', 'cogito', 'condign', 'conodont', 'conoid',
'coondog', 'incidit', 'indic', 'indiction', 'abfarad', 'daraf', 'draff', 'offroad', 'fallboard', 'boof', 'bete', 'beth', 'bethel', 'betty', 'bitty', 'lethe', 'libet', 'lilith', 'tebet', 'thebe', 'thill', 'tibet', 'titbit', 'montana', 'montanan',
'naphtha', 'naptha', 'phonanta', 'tampa', 'demel', 'demele', 'dolmen', 'endome', 'leonem', 'lome', 'medendo', 'meed', 'mendel', 'modelled', 'monde', 'omnem', 'alcaid', 'catacala', 'tacca', 'annapurna', 'loup', 'lupanar', 'parula', 'paulo', 'ppour',
'purana', 'purloo', 'purpura', 'roup', 'anoplura', 'acholia', 'aitch', 'cachalot', 'cahita', 'cahoot', 'cahot', 'caltha', 'chait', 'chatti', 'chiococca', 'cholla', 'clich', 'clotho', 'cotacachi', 'haiti', 'halloa', 'halloo', 'holloa', 'lathi', 
'lich', 'lithic', 'ohio', 'tahiti', 'thai', 'thaila', 'catholical', 'tallith', 'loth', 'thalia', 'mazama', 'mezee', 'zama', 'zambo', 'zambomba', 'zembla', 'zomba', 'amari', 'armillaria', 'ilama', 'imprimit', 'lamia', 'lamplit', 'limpa',
'mali', 'malta', 'mammalia', 'mammilla', 'mammillaria', 'marattia', 'mari', 'maria', 'marial', 'militat', 'mitra', 'pima', 'priam', 'prima', 'talma', 'tamil', 'timalia', 'acta', 'addax', 'avec', 'deat', 'detat', 'edax', 'taxaceae', 'vexata',
'teteatete', 'gluon', 'gulo', 'lough', 'aleppo', 'apocope', 'apollo', 'bopeep', 'collop', 'colpocele', 'copal', 'epopoca', 'peba', 'peccable', 'ploce', 'polacca', 'placable')


word_list = word_list.difference(remove_words)


bee_spoiler(word_list, "p", "lbcoae")



 
  


