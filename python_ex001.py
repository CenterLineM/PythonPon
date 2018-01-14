Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help("modules")

Please wait a moment while I gather a list of all available modules...

AutoComplete        _markerlib          fractions           repr
AutoCompleteWindow  _md5                ftplib              rexec
AutoExpand          _msi                functools           rfc822
BaseHTTPServer      _multibytecodec     future_builtins     rlcompleter
Bastion             _multiprocessing    gc                  robotparser
Bindings            _osx_support        genericpath         rpc
CGIHTTPServer       _pyio               getopt              run
CallTipWindow       _random             getpass             runpy
CallTips            _sha                gettext             sched
Canvas              _sha256             glob                select
ClassBrowser        _sha512             gzip                sets
CodeContext         _socket             hashlib             setuptools
ColorDelegator      _sqlite3            heapq               sgmllib
ConfigParser        _sre                hmac                sha
Cookie              _ssl                hotshot             shelve
Debugger            _strptime           htmlentitydefs      shlex
Delegator           _struct             htmllib             shutil
Dialog              _subprocess         httplib             signal
DocXMLRPCServer     _symtable           idle                site
EditorWindow        _testcapi           idle_test           smtpd
FileDialog          _threading_local    idlelib             smtplib
FileList            _tkinter            idlever             sndhdr
FixTk               _warnings           ihooks              socket
FormatParagraph     _weakref            imageop             sqlite3
GrepDialog          _weakrefset         imaplib             sre
HTMLParser          _winreg             imghdr              sre_compile
HyperParser         abc                 imp                 sre_constants
IOBinding           aboutDialog         importlib           sre_parse
IdleHistory         aifc                imputil             ssl
MimeWriter          antigravity         inspect             stat
MultiCall           anydbm              io                  statvfs
MultiStatusBar      argparse            itertools           string
ObjectBrowser       array               json                stringold
OutputWindow        ast                 keybindingDialog    stringprep
ParenMatch          asynchat            keyword             strop
PathBrowser         asyncore            lib2to3             struct
Percolator          atexit              linecache           subprocess
PyParse             audiodev            locale              sunau
PyShell             audioop             logging             sunaudio
Queue               base64              macosxSupport       symbol
RemoteDebugger      bdb                 macpath             symtable
RemoteObjectBrowser binascii            macurl2path         sys
ReplaceDialog       binhex              mailbox             sysconfig
RstripExtension     bisect              mailcap             tabbedpages
ScriptBinding       bsddb               markupbase          tabnanny
ScrolledList        bz2                 marshal             tarfile
ScrolledText        cPickle             math                telnetlib
SearchDialog        cProfile            md5                 tempfile
SearchDialogBase    cStringIO           mhlib               test
SearchEngine        calendar            mimetools           textView
SimpleDialog        cgi                 mimetypes           textwrap
SimpleHTTPServer    cgitb               mimify              this
SimpleXMLRPCServer  chunk               mmap                thread
SocketServer        cmath               modulefinder        threading
StackViewer         cmd                 msilib              time
StringIO            code                msvcrt              timeit
Tix                 codecs              multifile           tkColorChooser
Tkconstants         codeop              multiprocessing     tkCommonDialog
Tkdnd               collections         mutex               tkFileDialog
Tkinter             colorsys            netrc               tkFont
ToolTip             commands            new                 tkMessageBox
TreeWidget          compileall          nntplib             tkSimpleDialog
UndoDelegator       compiler            nt                  toaiff
UserDict            configDialog        ntpath              token
UserList            configHandler       nturl2path          tokenize
UserString          configHelpSourceEdit numbers             trace
WidgetRedirector    configSectionNameDialog opcode              traceback
WindowList          contextlib          operator            ttk
ZoomHeight          cookielib           optparse            tty
_LWPCookieJar       copy                os                  turtle
_MozillaCookieJar   copy_reg            os2emxpath          types
__builtin__         csv                 parser              unicodedata
__future__          ctypes              pdb                 unittest
_abcoll             curses              pickle              urllib
_ast                datetime            pickletools         urllib2
_bisect             dbhash              pip                 urlparse
_bsddb              decimal             pipes               user
_codecs             difflib             pkg_resources       uu
_codecs_cn          dircache            pkgutil             uuid
_codecs_hk          dis                 platform            warnings
_codecs_iso2022     distutils           plistlib            wave
_codecs_jp          doctest             popen2              weakref
_codecs_kr          dumbdbm             poplib              webbrowser
_codecs_tw          dummy_thread        posixfile           whichdb
_collections        dummy_threading     posixpath           winsound
_csv                dynOptionMenuWidget pprint              wsgiref
_ctypes             easy_install        profile             xdrlib
_ctypes_test        email               pstats              xml
_elementtree        encodings           pty                 xmllib
_functools          ensurepip           py_compile          xmlrpclib
_hashlib            errno               pyclbr              xxsubtype
_heapq              exceptions          pydoc               zipfile
_hotshot            filecmp             pydoc_data          zipimport
_io                 fileinput           pyexpat             zlib
_json               fnmatch             quopri              
_locale             formatter           random              
_lsprof             fpformat            re                  

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose descriptions contain the word "spam".

>>> len(pet)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    len(pet)
NameError: name 'pet' is not defined
>>> three = 3
>>> four = 4
>>> result = three * four
>>> result
12
>>> pet

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pet
NameError: name 'pet' is not defined
>>> lottery = [4 , 45 , 34 , 97 , 289]
>>> len(lottery)
5
>>> lottery[-1]
289
>>> 
