N = 714592249192120574265549436543825320509297072460484908344551300848373950674709416392248163503009591432801798300330358178220254883717911157090135486421989552552147396621456254872283054955425283572036333491216951659148637315743959395586665559407519185229157300079108262693898276136247810534552392553906737985611110264448201843163865017096262294351114549098951322813773897128719465176150883053986360952304498383310610388460484237430349371244701530043497920108895863314684142551140747512422595886581301888713595118142132885185198303308800502507859896464969717683441407760870801008449528112153549212478276556675394023846309427093179585325018415263363711804378835430582617669093961332068476235704892048030162691875630153887077065312965169814482719773409530562723633263914554200418602183589129968965528779239961904500471047970125553055971852444341804468217884681958789030613269002628729535741593441270914269404131869255645026880452432270622768454312090491642808585493953483725812286848383476643016688161197575479969967473807170678498031626472112346403780703388369738886890609192785409171065537393615632007758402675797183887353336941500878253793896387519274154235995528408268372482120436448099799778471121984170778048507949923503459997465919
e = 65537
NZ = 643363792440934119366912614785585611207080300686189925502975029733171061374272764555471159389382836710126848893211367235694279698304288443884055857979749856654105125890185467163471932733810535029345075012281405600410062774126198780350429996223340150530610063234814369421328149216616660714944177144017407519385830408002305903726852593916719173489869258332682896050832359636346814341162169049414603101956886466360467492876367002637470510425647057320597047428284251430565832687057079032309440909695667583068192363848168058084157820198423286886166957625051081629048570694819279810628012100796058478208742817600162176624758369843705785990733906771064313211605441231074320904990176643974726068792117474423505770153019434573197622007025942413749968190437680500002235880134734177685069908351640555727668710885989701656801820845100645158768502890163470606806278248531131762743743917250546667835937495858493058558362452062617428908615957036257930376984081719222258605410511547591258186531055130577843766423876717208678139899702143214838895715945841682068301332514907250357969801436529623882940121204403559167341066392029948206595220431231392884864675310409040301327860953357204012107578320395973686245176422713727709152784877348155727352671711

C = 70449696263904853205021769421025450507634290026721727701857926047437310331955388930964220695464570272172353035007329664946412219561278110997087844911854667398353605863465768216993861667525986599313398611428022273648895856421230118795282916445349033209350994570414487276471713417804733725499960083720555564092067927613175905501295302281765595762073475909299272903276376309567672479298763204244928980509067193939204965243351377923460364254060105896875660841061381226810596833539554263093079263716154660210358586976575152404111717726722071223917174024015283232917986634901529389619864650651703216005451875700418866768927106385012044761959477027935671366261266392663153946230717548196882529907819937189916550823654087319816481994984924592719530346872842300830544615122555222355696374761930068829585754131130228339335623901493687703710739312116756315878037422902317964923149084174661962115014291725708283288061699504266990938813504278334174416920218812959792660788648394165708140385048570391313513204772637164172908897320213723508275982127719931818043247687283692425375996228257787805937183419862154951258356873515841327068445010210907359329244847644393770839437950372965918801434262476928451655510733531908781254969777784115130520140013
l = []
for i in range(1, N+1):
    if N % i == 0:
        l.append(i)
    else:
        print(i)

print(l)


