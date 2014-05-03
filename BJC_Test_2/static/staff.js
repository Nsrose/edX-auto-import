/*****************************************************************************/
/*
CS10 -- staff.js
This file builds the staff images section from JSON data and makes working with
these images much easier.
Here is a sample object (with all properties):
DanGarcia = {
    name: 'Sr. Lecturer SOE Dan Garcia',
    img: 'http://www.cs.berkeley.edu/~ddgarcia/gifs/DanGarciaUCBFaculty2004.jpg',
    imgSrc: 'DanGarcia.jpg',
    web: 'http://www.cs.berkeley.edu/%7Eddgarcia/',
    bio: 'DanBio.txt',
    email: 'ddgarcia@cs.berkeley.edu',
    office: '777 Soda, (510) 517-4041'
}

OR There is a simplified version for standard names:
BrandonChen = { name: 'Brandon Chen',
    img: 'Sp14/BrandonChen.jpg',
    imgSrc: 'BrandonChen.jpg' }
can be created with simply 'Brandon Chen' as a string in the appropriate lists.
NOTE: All images must be in the proper folders and match the name, w/o spaces.

You can create any objects like this. REQUIRED ARE: name, img, imgSrc
'imgSrc' should be a small image in the directory ~/public_html/images/small/ *

There are a few lists of objects:
instructors, tas, readers, las -- more can be created if necessary:
To add a new section:
1. Add a div with an ID to staff.html
2. Add the same ID name to the 'all' object.
3. Add a call to buildGroup(), with the ID name (string) and the number of
images per row (int)
*/
/*****************************************************************************/

// JSON mappings for staff images / info.

///////////////////////////////////////////////////////// Instructors
DanGarcia = {
    name: 'Sr. Lecturer SOE Dan Garcia',
    img: 'DanGarciaUCBFaculty2004.jpg',
    imgSrc: 'DanGarcia.jpg',
    web: 'http://www.cs.berkeley.edu/%7Eddgarcia/',
    bio: 'DanBio.txt',
    email: 'ddgarcia@cs.berkeley.edu',
    office: '777 Soda, (510) 517-4041'
}

///////////////////////////////////////////////////////// TAs
MichaelBall = {
    name: 'Head TA Michael Ball',
    img: 'Sp14/MichaelBallTake3.jpg',
    imgSrc: 'MichaelBall.jpg',
    web: 'http://michaelballphoto.com',
    bio: 'MichaelBall.txt',
    email: 'cs10-ta@imail.eecs.berkeley.edu'
}
maxD = {
    name: 'TA Max Dougherty',
    img: 'Sp14/MaxDougherty.jpg',
    imgSrc: 'MaxDougherty.jpg',
    email: 'mdougherty@berkeley.edu'
}
IanBirnam = {
    name: 'TA Ian Birnam',
    img: 'Sp14/IanBirnam.jpg',
    imgSrc: 'IanBirnam.jpg',
    web: 'http://ianbirnam.com',
    bio: 'IanBio.txt',
    email: 'ibirnam@berkeley.edu'
}
jeffreyS = {
    name: 'TA Jeffrey Snowiss',
    img: 'Fa12/JeffreySnowiss.jpg',
    imgSrc: 'JeffreySnowiss.jpg',
    email: 'jasnowiss10@gmail.com'
}
PeterSujan = {
    name: 'TA Peter Sujan',
    img: 'Fa12/PeterSujan.jpg',
    imgSrc: 'PeterSujan.jpg',
    bio: 'PeterBio.txt',
    email: 'peterasujan@berkeley.edu'
}
victoriaS = {
    name: 'TA Victoria Shi',
    img: 'Fa13/VictoriaShi.jpg',
    imgSrc: 'VictoriaShi.jpg',
    email: 'victoria.shi@berkeley.edu'
}
rachelH = {
    name: 'TA Rachel Huang',
    img: 'Fa13/RachelHuang.jpg',
    imgSrc: 'RachelHuang.jpg',
    email: 'rachelhuang072@berkeley.edu'
}
jannaG = {
    name: 'TA Janna Golden',
    img: 'Sp14/JannaGolden.jpg',
    imgSrc: 'JannaGolden.jpg',
    email: 'jannagolden@berkeley.edu'
}
sumerM = {
    name: 'TA Sumer Mohammed',
    img: 'Fa12/SumerMohammed.jpg',
    imgSrc: 'SumerMohammed.jpg',
    email: 'sumermohammed@berkeley.edu' }

///////////////////////////////////////////////////////// Readers
josephC = {
    name: 'Reader Joseph Cawthorne',
    img: 'Fa13/JosephCawthorne.jpg',
    imgSrc: 'JosephCawthorne.jpg' }
songS   = {
    name: 'Reader Song Sok',
    img: 'Fa13/SongSok.jpg',
    imgSrc: 'SongSok.jpg' }
claireW = {
    name: 'Reader Claire Watanabe',
    img: 'Fa13/ClaireWatanabe.jpg',
    imgSrc: 'ClaireWatanabe.jpg' }
jaclynB = {
    name: 'Reader Jaclyn Burge',
    img: 'Fa13/JaclynBurge.jpg',
    imgSrc: 'JaclynBurge.jpg' }
andyS   = {
    name: 'Reader Andrew Schmitt',
    img: 'Sp14/AndrewSchmitt.jpg',
    imgSrc: 'AndrewSchmitt.jpg' }

///////////////////////////////////////////////////////// Staff
LaurenMock = {
    name: 'Project Manager Lauren Mock',
    img: 'Sp14/LaurenMock.jpg',
    imgSrc: 'LaurenMock.jpg',
    web: 'http://linkedin.com/in/laurenmock',
    email: 'lmock@berkeley.edu'
}

///////////////////////////////////////////////////////// edX
KunalMarwaha = { name: 'edX Team Lead Kunal Marwaha',
    img: 'Sp14/KunalMarwaha.jpg',
    imgSrc: 'KunalMarwaha.jpg',
    email: 'marwahaha@berkeley.edu'
    }

///////////////////////////////////////////////////////// Snap
KyleZentner = { name: 'Snap! Team Lead Kyle Zentner',
    img: 'Sp14/KyleZentner.jpg',
    imgSrc: 'KyleZentner.jpg' }

JocelynTakahashi = { name: 'Jocelyn Takahashi',
    img: 'Sp13/JocelynTakahashi.jpg',
    imgSrc: '../Sp13/t/JocelynTakahashi.jpg' }

///////////////////////////////////////////////////////// Lab Assistants
///////////////////////////////////////////////////////// TAiT -- TAiT is auto added
benC = { name: 'Ben Carvalho',
    img: 'Fa13/BenCarvalho.jpg',
    imgSrc: 'BenCarvalho.jpg',
    bio: 'BenjaminCarvalhoBio.txt' }
oliverO = { name: 'Oliver O\'Donnell',
    img: 'Sp14/OliverODonnell.jpg',
    imgSrc: 'OliverODonnell.jpg',
    bio: 'Oliver ODonnell.txt' }
carenT = { name: 'Caren Thomas',
    img: 'Sp14/CarenThomas.jpg',
    imgSrc: 'CarenThomas.jpg',
    bio: 'CarenThomasBio.txt' }

///////////////////////////////////////////////////////// Lab Dev
paulI = { name: 'Paul Irwin',
    img: 'Fa13/PaulIrwin.jpg',
    imgSrc: 'PaulIrwin.jpg' }

jessicaA = { name: 'Jessica Andrich',
    img: 'Fa13/JessicaAndrich.jpg',
    imgSrc: 'JessicaAndrich.jpg' }
    


/*****************************************************************************/
/** LIST DEFINITIONS **/
/*****************************************************************************/

instructors = [ DanGarcia ];

tas = [ LaurenMock, jannaG, rachelH, sumerM, victoriaS, MichaelBall,
        IanBirnam, jeffreyS, maxD, PeterSujan ]

readers = [ andyS, claireW, jaclynB, josephC, songS ]

las = [ 'Adam Brown',
        'Alex Freeman',
        'Alison Tang',
        'Amruta Yelamanchili',
        'Amy Shu',
        'Brooke Tencer',
        'Bryce Smith',
        'Caroline Chan',
        'Charles Thorson',
        'Fangzhou Chen',
        'Franklin Lee',
        'Gurubala Kotta',
        'Harris Quraishi',
        'Helen Hu',
        'Itzel Martinez',
        'Jason Do',
        'Jiawei Will Jiang',
        'Ji Jun Chen',
        'Joel Terry',
        'Kalon Cheung',
        'Kyla Sorin',
        'Liuxiao Zhang',
        'Maria Can',
        'Mateo O Marin',
        'Michelle Han',
        'Mohan Ganesan',
        'Mona Lee',
        'Navsharan Singh',
        'Nicholas Dill',
        'Nick Rose',
        'Priscilla Bermudez',
        'Ryan Riddle',
        'Steven Holman',
        'Tammy Chen',
        'Tierney Henderson',
        'Victoria Bian',
        'Victor Solis',
        'Yibing Chen' ]

tait = [ benC, songS, josephC, andyS,
    'Adam Kuphaldt',
    'Alex McKinney',
    'Arany Uthayakumar',
    'Brandon Chen',
    'Carlos Flores',
    carenT,
    'Christopher Kilian',
    'Derek Chiu',
    'Edwan Hernandez',
    'Hunter Brown',
    'Jeffrey Jacinto',
    'Jobel Vecino',
    'Josh Perline',
    'Kalley Thompson',
    'Kwan Cheung',
    'Luke Dodds',
    'Michelle Tsai',
    'Nolan Takeshita',
    oliverO,
    'Rafayel Mkrtchyan',
    'Saagar Bakshi',
    'Sean Scofield',
    'Steven Traversi',
    'Sulaiman Haruna',
    'Veersuvrat Rajpal' ]

labdev = [ PeterSujan, LaurenMock, jessicaA, paulI, andyS, 'Liuxiao Zhang',
           'Manisha Sharma', 'Samy Hajal', 'Sulaiman Haruna' ]

edx = [ KunalMarwaha, 
        LaurenMock, 
        josephC, 
        'Sean Scofield', 
        'Akhila Raju',
        'Alex Chao',
        'Harsh Mujoo',
        'Josh Perline',
        'Kevin Chen',
        'Manisha Sharma',
        'Mrindula Dilip',
        'Nick Rose',
        'Nidhi Swamy',
        'Patrick Lu',
        'Rebecca Kuan',
        'Saeam Kwon',
        'Sneha Dilip',
        songS,
        'Sophie Cooper',
        'Stephen Shan'  ]

snap = [ KunalMarwaha,  
         KyleZentner, 
         'Aaron Yuan',
         'Andy Cheon',
         'Angela So',
         'Ashkan Hosseini',
         'Brandon Chen',
         'Carlos Flores',
         'Dibyo Majundar',
         'Elizabeth Stella Walla',
         'Farzin Jahani',
         'Gilbert Ghang',
         'Irene Lee',
         'Janet Chu',
         'Jesar Shah',
         'Jisoo Han',
         'Joanne Xu',
         JocelynTakahashi,
         'Joey Barreto',
         'Kyle Hotchkiss',
         'Lingtian Cheng',
         'Michelle Han',
         'Mohan Ganesan',
         'Natasha Sandy',
         'Randy Wei',
         'Sara Seacat',
         'Tanisha Singh',
         'Tanvi Kamath',
         'Yuan Yuan' ]

bjc = [ LaurenMock, MichaelBall, PeterSujan, KunalMarwaha, KyleZentner ]


// If you need to add a new SECTION add it to this object.
// Follow the same format.
all = {
    instructors: instructors,
    las: las,
    readers: readers,
    tas: tas,
    tait: tait,
    edx: edx,
    snap: snap,
    labdev: labdev,
    bjc: bjc
};

//LOL - Ian
LIST_OF_SHAME = [
'AngelaSo.jpg',
'HarshMujoo.jpg',
'HunterBrown.jpg',
'IreneLee.jpg',
'JesarShah.jpg',
'JiJunChen.jpg',
'JisooHan.jpg',
'MichelleHan.jpg',
'NavsharanSingh.jpg',
'NicholasDill.jpg',
'PriscillaBermudez.jpg',
'RebeccaKuan.jpg',
'SamyHajal.jpg',
'SerenaChan.jpg',
'StephenShan.jpg',
'StevenHolman.jpg',
'VictorSolis.jpg' ]

// Prepend TAiT to names, except for Readers.
for(var i = 0; i < tait.length; i++) {
    if (tait[i].constructor === String) {
        tait[i] = baseObj(tait[i])
    }

    if (tait[i].name.indexOf('Reader') === -1) {
        tait[i].name = 'TAiT ' + tait[i].name
    }
}
/*****************************************************************************/
/* DATA POPULATION FUNCTIONS  */
/*****************************************************************************/

// Build a basic object for a person from the current semester.
function baseObj(name) {
    src = name.replace(/ /g , '')
    return { name: name,
             img: 'Sp14/' + src + '.jpg',
             imgSrc: src + '.jpg' }
}

function buildPerson(data, width) {
    // Given a JSON object build a div that contains all the person's info
    // width is used to control how many are on a row on the page.

    // Build data objects for very simple cases with nothing special.
    if (data.constructor === String) {
        data = baseObj(data)
    }

    // If there's no image, use 3D Alanzo
    if (!data.imgSrc || LIST_OF_SHAME.indexOf(data.imgSrc) !== -1) {
        data.imgSrc = '../NPY3D.jpg'
        data.img    = ''
    }
    // Create a table element with this person's data, setting a class for width
    elm = '<div style="width:' + 100/width + '%;">'
    if (!!data.img) {
        elm += '<a href=\'https://inst.eecs.berkeley.edu/~cs10/sp14/images/' + data.img + '\'>'
    }
    elm += '<img class=\'staff\' width=\'200\' height=\'300\' align=\'center\' '
    elm += 'alt=\'' + data.name + '\' title=\'' + data.name + '\' src=\'https://inst.eecs.berkeley.edu/~cs10/sp14/images/small/'
    elm += data.imgSrc + '\' />'
    if (!!data.img) {
        elm += '</a>'
    }
    elm += '<br /><strong>'
    if (!!data.web) {
        elm += '<a href=\'' + data.web + '\'>' + data.name + '</a>'
    } else {
        elm += data.name
    }
    elm += '</strong> '
    if (!!data.bio) {
        elm += '(<a href=\'bios/' + data.bio + '\'>bio</a>)'
    }
    if (!!data.email) {
        elm += '<br /><a style=\'font-size:10px\' href=\'mailto:' + data.email +
        '?subject=[CS10] SUBJECT\'><code style=\'font-size:10px\'>' + data.email + '</code></a>';
    }
    if (!!data.office) {
        elm +=  '<br />' + data.office
    }
    elm += '</div>';
    return elm;
}

function buildGroup(group, w) {
    // Build a set of table rows, with W items per row
    // based on the people in the GROUP
    // Add them to the appropriate HTML table element
    ppl = all[group]
    doc = document.getElementById(group)
    content = ''
    for (var i = 0; i < ppl.length; i += w) {
        content += '<div style=\'margin-bottom:10px\' class=\'staffimg\'>'
        for(var j = i; j < (i + w) && j < ppl.length; j += 1) {
            if (i + w > ppl.length) {
                 w = ppl.length - i
             }
            content += buildPerson(ppl[j], w)
        }
        content += '</div>'
        // content += '<div style=\'clear: both;\'></div>';
    }
    doc.innerHTML += content
}

function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      if (oldonload) {
        oldonload();
      }
      func();
    }
  }
}

addLoadEvent(function() {
  /* more code to run on page load */
  // Parameters: a section (HTML 'id') and num of images per row.
  buildGroup('instructors', 1)
  buildGroup('tas', 5)
  buildGroup('readers', 5)
  buildGroup('tait', 5)
  buildGroup('las', 5)
  buildGroup('edx', 5)
  buildGroup('labdev', 5)
  buildGroup('snap', 5)
  buildGroup('bjc', 5)
})