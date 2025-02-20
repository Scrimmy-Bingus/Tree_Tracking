from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the game
@app.route('/game')
def game():
    return render_template('index.html')

@app.route('/afghanistan')
def afghanistan():
    return render_template('info/afghanistan.html')

@app.route('/albania')
def albania():
    return render_template('info/albania.html')

@app.route('/algeria')
def algeria():
    return render_template('info/algeria.html')

@app.route('/angola')
def angola():
    return render_template('info/angola.html')

@app.route('/argentina')
def argentina():
    return render_template('info/argentina.html')

@app.route('/armenia')
def armenia():
    return render_template('info/armenia.html')

@app.route('/australia')
def australia():
    return render_template('info/australia.html')

@app.route('/austria')
def austria():
    return render_template('info/austria.html')

@app.route('/azerbaijan')
def azerbaijan():
    return render_template('info/azerbaijan.html')

@app.route('/bangladesh')
def bangladesh():
    return render_template('info/bangladesh.html')

@app.route('/belarus')
def belarus():
    return render_template('info/belarus.html')

@app.route('/belgium')
def belgium():
    return render_template('info/belgium.html')

@app.route('/benin')
def benin():
    return render_template('info/benin.html')

@app.route('/bhutan')
def bhutan():
    return render_template('info/bhutan.html')

@app.route('/bolivia')
def bolivia():
    return render_template('info/bolivia.html')

@app.route('/bosnia-and-herzegovina')
def bosnia_and_herzegovina():
    return render_template('info/bosnia-and-herzegovina.html')

@app.route('/botswana')
def botswana():
    return render_template('info/botswana.html')

@app.route('/brazil')
def brazil():
    return render_template('info/brazil.html')

@app.route('/bulgaria')
def bulgaria():
    return render_template('info/bulgaria.html')

@app.route('/burkina-faso')
def burkina_faso():
    return render_template('info/burkina-faso.html')

@app.route('/burundi')
def burundi():
    return render_template('info/burundi.html')

@app.route('/cambodia')
def cambodia():
    return render_template('info/cambodia.html')

@app.route('/cameroon')
def cameroon():
    return render_template('info/cameroon.html')

@app.route('/canada')
def canada():
    return render_template('info/canada.html')

@app.route('/central-african-republic')
def central_african_republic():
    return render_template('info/central-african-republic.html')

@app.route('/chad')
def chad():
    return render_template('info/chad.html')

@app.route('/chile')
def chile():
    return render_template('info/chile.html')

@app.route('/china')
def china():
    return render_template('info/china.html')

@app.route('/colombia')
def colombia():
    return render_template('info/colombia.html')

@app.route('/cote-divoire')
def cote_divoire():
    return render_template('info/cote-divoire.html')

@app.route('/croatia')
def croatia():
    return render_template('info/croatia.html')

@app.route('/cuba')
def cuba():
    return render_template('info/cuba.html')

@app.route('/czech-republic')
def czech_republic():
    return render_template('info/czech-republic.html')

@app.route('/democratic-republic-of-the-congo')
def democratic_republic_of_the_congo():
    return render_template('info/democratic-republic-of-the-congo.html')

@app.route('/denmark')
def denmark():
    return render_template('info/denmark.html')

@app.route('/dominican-republic')
def dominican_republic():
    return render_template('info/dominican-republic.html')

@app.route('/ecuador')
def ecuador():
    return render_template('info/ecuador.html')

@app.route('/egypt')
def egypt():
    return render_template('info/egypt.html')

@app.route('/el-salvador')
def el_salvador():
    return render_template('info/el-salvador.html')

@app.route('/ethiopia')
def ethiopia():
    return render_template('info/ethiopia.html')

@app.route('/fiji')
def fiji():
    return render_template('info/fiji.html')

@app.route('/finland')
def finland():
    return render_template('info/finland.html')

@app.route('/france')
def france():
    return render_template('info/france.html')

@app.route('/gabon')
def gabon():
    return render_template('info/gabon.html')

@app.route('/gambia')
def gambia():
    return render_template('info/gambia.html')

@app.route('/georgia')
def georgia():
    return render_template('info/georgia.html')

@app.route('/germany')
def germany():
    return render_template('info/germany.html')

@app.route('/ghana')
def ghana():
    return render_template('info/ghana.html')

@app.route('/greece')
def greece():
    return render_template('info/greece.html')

@app.route('/guatemala')
def guatemala():
    return render_template('info/guatemala.html')

@app.route('/guinea')
def guinea():
    return render_template('info/guinea.html')

@app.route('/guyana')
def guyana():
    return render_template('info/guyana.html')

@app.route('/haiti')
def haiti():
    return render_template('info/haiti.html')

@app.route('/honduras')
def honduras():
    return render_template('info/honduras.html')

@app.route('/hungary')
def hungary():
    return render_template('info/hungary.html')

@app.route('/india')
def india():
    return render_template('info/india.html')

@app.route('/indonesia')
def indonesia():
    return render_template('info/indonesia.html')

@app.route('/iran')
def iran():
    return render_template('info/iran.html')

@app.route('/iraq')
def iraq():
    return render_template('info/iraq.html')

@app.route('/israel')
def israel():
    return render_template('info/israel.html')

@app.route('/italy')
def italy():
    return render_template('info/italy.html')

@app.route('/jamaica')
def jamaica():
    return render_template('info/jamaica.html')

@app.route('/japan')
def japan():
    return render_template('info/japan.html')

@app.route('/jordan')
def jordan():
    return render_template('info/jordan.html')

@app.route('/kazakhstan')
def kazakhstan():
    return render_template('info/kazakhstan.html')

@app.route('/kenya')
def kenya():
    return render_template('info/kenya.html')

@app.route('/kiribati')
def kiribati():
    return render_template('info/kiribati.html')

@app.route('/korea-south')
def korea_south():
    return render_template('info/korea-south.html')

@app.route('/kuwait')
def kuwait():
    return render_template('info/kuwait.html')

@app.route('/kyrgyzstan')
def kyrgyzstan():
    return render_template('info/kyrgyzstan.html')

@app.route('/laos')
def laos():
    return render_template('info/laos.html')

@app.route('/latvia')
def latvia():
    return render_template('info/latvia.html')

@app.route('/lebanon')
def lebanon():
    return render_template('info/lebanon.html')

@app.route('/lesotho')
def lesotho():
    return render_template('info/lesotho.html')

@app.route('/liberia')
def liberia():
    return render_template('info/liberia.html')

@app.route('/libya')
def libya():
    return render_template('info/libya.html')

@app.route('/lithuania')
def lithuania():
    return render_template('info/lithuania.html')

@app.route('/luxembourg')
def luxembourg():
    return render_template('info/luxembourg.html')

@app.route('/madagascar')
def madagascar():
    return render_template('info/madagascar.html')

@app.route('/malawi')
def malawi():
    return render_template('info/malawi.html')

@app.route('/malaysia')
def malaysia():
    return render_template('info/malaysia.html')

@app.route('/mali')
def mali():
    return render_template('info/mali.html')

@app.route('/mauritania')
def mauritania():
    return render_template('info/mauritania.html')

@app.route('/mauritius')
def mauritius():
    return render_template('info/mauritius.html')

@app.route('/mexico')
def mexico():
    return render_template('info/mexico.html')

@app.route('/moldova')
def moldova():
    return render_template('info/moldova.html')

@app.route('/mongolia')
def mongolia():
    return render_template('info/mongolia.html')

@app.route('/montenegro')
def montenegro():
    return render_template('info/montenegro.html')

@app.route('/morocco')
def morocco():
    return render_template('info/morocco.html')

@app.route('/mozambique')
def mozambique():
    return render_template('info/mozambique.html')

@app.route('/myanmar')
def myanmar():
    return render_template('info/myanmar.html')

@app.route('/namibia')
def namibia():
    return render_template('info/namibia.html')

@app.route('/nepal')
def nepal():
    return render_template('info/nepal.html')

@app.route('/netherlands')
def netherlands():
    return render_template('info/netherlands.html')

@app.route('/new-zealand')
def new_zealand():
    return render_template('info/new-zealand.html')

@app.route('/nicaragua')
def nicaragua():
    return render_template('info/nicaragua.html')

@app.route('/niger')
def niger():
    return render_template('info/niger.html')

@app.route('/nigeria')
def nigeria():
    return render_template('info/nigeria.html')

@app.route('/north-korea')
def north_korea():
    return render_template('info/north-korea.html')

@app.route('/norway')
def norway():
    return render_template('info/norway.html')

@app.route('/oman')
def oman():
    return render_template('info/oman.html')

@app.route('/pakistan')
def pakistan():
    return render_template('info/pakistan.html')

@app.route('/panama')
def panama():
    return render_template('info/panama.html')

@app.route('/papua-new-guinea')
def papua_new_guinea():
    return render_template('info/papua-new-guinea.html')

@app.route('/paraguay')
def paraguay():
    return render_template('info/paraguay.html')

@app.route('/peru')
def peru():
    return render_template('info/peru.html')

@app.route('/philippines')
def philippines():
    return render_template('info/philippines.html')

@app.route('/poland')
def poland():
    return render_template('info/poland.html')

@app.route('/portugal')
def portugal():
    return render_template('info/portugal.html')

@app.route('/qatar')
def qatar():
    return render_template('info/qatar.html')

@app.route('/romania')
def romania():
    return render_template('info/romania.html')

@app.route('/russia')
def russia():
    return render_template('info/russia.html')

@app.route('/rwanda')
def rwanda():
    return render_template('info/rwanda.html')

@app.route('/saudi-arabia')
def saudi_arabia():
    return render_template('info/saudi-arabia.html')

@app.route('/senegal')
def senegal():
    return render_template('info/senegal.html')

@app.route('/serbia')
def serbia():
    return render_template('info/serbia.html')

@app.route('/sierra-leone')
def sierra_leone():
    return render_template('info/sierra-leone.html')

@app.route('/singapore')
def singapore():
    return render_template('info/singapore.html')

@app.route('/slovakia')
def slovakia():
    return render_template('info/slovakia.html')

@app.route('/slovenia')
def slovenia():
    return render_template('info/slovenia.html')

@app.route('/somalia')
def somalia():
    return render_template('info/somalia.html')

@app.route('/south-africa')
def south_africa():
    return render_template('info/south-africa.html')

@app.route('/south-sudan')
def south_sudan():
    return render_template('info/south-sudan.html')

@app.route('/spain')
def spain():
    return render_template('info/spain.html')

@app.route('/sri-lanka')
def sri_lanka():
    return render_template('info/sri-lanka.html')

@app.route('/sudan')
def sudan():
    return render_template('info/sudan.html')

@app.route('/suriname')
def suriname():
    return render_template('info/suriname.html')

@app.route('/sweden')
def sweden():
    return render_template('info/sweden.html')

@app.route('/switzerland')
def switzerland():
    return render_template('info/switzerland.html')

@app.route('/syria')
def syria():
    return render_template('info/syria.html')

@app.route('/taiwan')
def taiwan():
    return render_template('info/taiwan.html')

@app.route('/tajikistan')
def tajikistan():
    return render_template('info/tajikistan.html')

@app.route('/tanzania')
def tanzania():
    return render_template('info/tanzania.html')

@app.route('/thailand')
def thailand():
    return render_template('info/thailand.html')

@app.route('/togo')
def togo():
    return render_template('info/togo.html')

@app.route('/tunisia')
def tunisia():
    return render_template('info/tunisia.html')

@app.route('/turkey')
def turkey():
    return render_template('info/turkey.html')

@app.route('/turkmenistan')
def turkmenistan():
    return render_template('info/turkmenistan.html')

@app.route('/uganda')
def uganda():
    return render_template('info/uganda.html')


...


if __name__ == '__main__':
    app.run(debug=True)
