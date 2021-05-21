%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-v
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Patch0106:      texlive-bz#1442706-python-path.patch
Source0003:     texlive-licenses.tar.xz
Source1510:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showtags.tar.xz
Source1511:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showtags.doc.tar.xz
Source1512:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sort-by-letters.tar.xz
Source1513:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sort-by-letters.doc.tar.xz
Source1514:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/splitbib.tar.xz
Source1515:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/splitbib.doc.tar.xz
Source1673:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stmaryrd.tar.xz
Source1674:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stmaryrd.doc.tar.xz
Source1705:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skaknew.tar.xz
Source1706:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skaknew.doc.tar.xz
Source2058:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skull.tar.xz
Source2060:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sourcecodepro.tar.xz
Source2061:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sourcecodepro.doc.tar.xz
Source2062:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sourcesanspro.tar.xz
Source2063:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sourcesanspro.doc.tar.xz
Source2064:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sourceserifpro.tar.xz
Source2065:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sourceserifpro.doc.tar.xz
Source2066:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/starfont.tar.xz
Source2067:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/starfont.doc.tar.xz
Source2068:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/staves.tar.xz
Source2069:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/staves.doc.tar.xz
Source2071:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stix.tar.xz
Source2072:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stix.doc.tar.xz
Source2074:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/superiors.tar.xz
Source2075:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/superiors.doc.tar.xz
Source2144:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/symbol.tar.xz
Source2201:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/startex.tar.xz
Source2202:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/startex.doc.tar.xz
Source2250:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skak.tar.xz
Source2251:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skak.doc.tar.xz
Source2252:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sudoku.tar.xz
Source2253:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sudoku.doc.tar.xz
Source2255:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sudokubundle.tar.xz
Source2256:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sudokubundle.doc.tar.xz
Source2324:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shade.tar.xz
Source2325:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shade.doc.tar.xz
Source2326:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/systeme.tar.xz
Source2327:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/systeme.doc.tar.xz
Source2468:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sides.tar.xz
Source2469:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sides.doc.tar.xz
Source2470:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stage.tar.xz
Source2471:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stage.doc.tar.xz
Source2504:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simurgh.tar.xz
Source2505:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simurgh.doc.tar.xz
Source2651:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simplified-latex.doc.tar.xz
Source2652:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svg-inkscape.doc.tar.xz
Source2703:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/swebib.tar.xz
Source2704:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/swebib.doc.tar.xz
Source2994:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spanish-mx.tar.xz
Source2995:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spanish-mx.doc.tar.xz
Source3095:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfig.tar.xz
Source3096:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfig.doc.tar.xz
Source3282:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/smartdiagram.tar.xz
Source3283:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/smartdiagram.doc.tar.xz
Source3285:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spath3.tar.xz
Source3286:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spath3.doc.tar.xz
Source3288:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/swimgraf.tar.xz
Source3289:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/swimgraf.doc.tar.xz
Source3316:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svn-prov.tar.xz
Source3317:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svn-prov.doc.tar.xz
Source5198:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shadethm.tar.xz
Source5199:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shadethm.doc.tar.xz
Source5200:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shadow.tar.xz
Source5201:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shadow.doc.tar.xz
Source5202:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shadowtext.tar.xz
Source5203:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shadowtext.doc.tar.xz
Source5204:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shapepar.tar.xz
Source5205:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shapepar.doc.tar.xz
Source5206:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shdoc.tar.xz
Source5207:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shdoc.doc.tar.xz
Source5209:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shipunov.tar.xz
Source5210:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shipunov.doc.tar.xz
Source5211:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shorttoc.tar.xz
Source5212:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shorttoc.doc.tar.xz
Source5214:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/show2e.tar.xz
Source5215:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/show2e.doc.tar.xz
Source5217:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showcharinbox.tar.xz
Source5218:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showcharinbox.doc.tar.xz
Source5220:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showdim.tar.xz
Source5221:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showdim.doc.tar.xz
Source5222:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showexpl.tar.xz
Source5223:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showexpl.doc.tar.xz
Source5225:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showlabels.tar.xz
Source5226:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showlabels.doc.tar.xz
Source5228:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sidecap.tar.xz
Source5229:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sidecap.doc.tar.xz
Source5231:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sidenotes.tar.xz
Source5232:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sidenotes.doc.tar.xz
Source5234:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/silence.tar.xz
Source5235:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/silence.doc.tar.xz
Source5237:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simplecd.tar.xz
Source5238:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simplecd.doc.tar.xz
Source5240:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simplecv.tar.xz
Source5241:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simplecv.doc.tar.xz
Source5243:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simplewick.tar.xz
Source5244:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simplewick.doc.tar.xz
Source5246:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sitem.tar.xz
Source5247:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sitem.doc.tar.xz
Source5249:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skb.tar.xz
Source5250:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skb.doc.tar.xz
Source5252:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skdoc.tar.xz
Source5253:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skdoc.doc.tar.xz
Source5255:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skeycommand.tar.xz
Source5256:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skeycommand.doc.tar.xz
Source5257:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skeyval.tar.xz
Source5258:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skeyval.doc.tar.xz
Source5259:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skrapport.tar.xz
Source5260:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skrapport.doc.tar.xz
Source5262:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/slantsc.tar.xz
Source5263:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/slantsc.doc.tar.xz
Source5265:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/smalltableof.tar.xz
Source5266:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/smalltableof.doc.tar.xz
Source5267:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/smartref.tar.xz
Source5268:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/smartref.doc.tar.xz
Source5269:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/snapshot.tar.xz
Source5270:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/snapshot.doc.tar.xz
Source5272:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/snotez.tar.xz
Source5273:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/snotez.doc.tar.xz
Source5274:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/soul.tar.xz
Source5275:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/soul.doc.tar.xz
Source5277:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sparklines.tar.xz
Source5278:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sparklines.doc.tar.xz
Source5279:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sphack.tar.xz
Source5280:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sphack.doc.tar.xz
Source5284:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spot.tar.xz
Source5285:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spot.doc.tar.xz
Source5287:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spotcolor.tar.xz
Source5288:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spotcolor.doc.tar.xz
Source5289:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spreadtab.tar.xz
Source5290:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spreadtab.doc.tar.xz
Source5291:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spverbatim.tar.xz
Source5292:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spverbatim.doc.tar.xz
Source5294:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/srbook-mem.tar.xz
Source5295:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/srbook-mem.doc.tar.xz
Source5296:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/srcltx.tar.xz
Source5297:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/srcltx.doc.tar.xz
Source5299:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sseq.tar.xz
Source5300:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sseq.doc.tar.xz
Source5302:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sslides.tar.xz
Source5303:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sslides.doc.tar.xz
Source5304:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stack.tar.xz
Source5306:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stackengine.tar.xz
Source5307:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stackengine.doc.tar.xz
Source5308:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/standalone.tar.xz
Source5309:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/standalone.doc.tar.xz
Source5311:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statistik.tar.xz
Source5312:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statistik.doc.tar.xz
Source5314:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stdclsdv.tar.xz
Source5315:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stdclsdv.doc.tar.xz
Source5317:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stdpage.tar.xz
Source5318:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stdpage.doc.tar.xz
Source5320:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stex.tar.xz
Source5321:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stex.doc.tar.xz
Source5323:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/storebox.tar.xz
Source5324:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/storebox.doc.tar.xz
Source5326:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/storecmd.tar.xz
Source5327:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/storecmd.doc.tar.xz
Source5328:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stringstrings.tar.xz
Source5329:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stringstrings.doc.tar.xz
Source5331:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sttools.tar.xz
Source5332:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sttools.doc.tar.xz
Source5334:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stubs.tar.xz
Source5335:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stubs.doc.tar.xz
Source5336:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subdepth.tar.xz
Source5337:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subdepth.doc.tar.xz
Source5339:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subeqn.tar.xz
Source5340:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subeqn.doc.tar.xz
Source5342:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subeqnarray.tar.xz
Source5343:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subeqnarray.doc.tar.xz
Source5345:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfigmat.tar.xz
Source5346:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfigmat.doc.tar.xz
Source5347:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfigure.tar.xz
Source5348:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfigure.doc.tar.xz
Source5350:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfiles.tar.xz
Source5351:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfiles.doc.tar.xz
Source5353:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfloat.tar.xz
Source5354:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subfloat.doc.tar.xz
Source5356:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/substitutefont.tar.xz
Source5357:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/substitutefont.doc.tar.xz
Source5358:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/substr.tar.xz
Source5359:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/substr.doc.tar.xz
Source5360:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/supertabular.tar.xz
Source5361:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/supertabular.doc.tar.xz
Source5363:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svg.tar.xz
Source5364:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svg.doc.tar.xz
Source5366:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svgcolor.tar.xz
Source5367:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svgcolor.doc.tar.xz
Source5368:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svn.tar.xz
Source5369:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svn.doc.tar.xz
Source5374:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svninfo.tar.xz
Source5375:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svninfo.doc.tar.xz
Source5377:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/syntax.tar.xz
Source5378:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/syntax.doc.tar.xz
Source5379:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/syntrace.tar.xz
Source5380:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/syntrace.doc.tar.xz
Source5382:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/synttree.tar.xz
Source5383:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/synttree.doc.tar.xz
Source5817:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showhyphens.tar.xz
Source5818:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/showhyphens.doc.tar.xz
Source5819:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spelling.tar.xz
Source5820:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spelling.doc.tar.xz
Source5901:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shuffle.tar.xz
Source5902:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shuffle.doc.tar.xz
Source5904:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skmath.tar.xz
Source5905:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/skmath.doc.tar.xz
Source5907:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statex.tar.xz
Source5908:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statex.doc.tar.xz
Source5909:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statex2.tar.xz
Source5910:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statex2.doc.tar.xz
Source5911:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subsupscripts.tar.xz
Source5912:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/subsupscripts.doc.tar.xz
Source5913:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/susy.tar.xz
Source5914:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/susy.doc.tar.xz
Source5915:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/syllogism.tar.xz
Source5916:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/syllogism.doc.tar.xz
Source5917:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sympytexpackage.tar.xz
Source5918:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sympytexpackage.doc.tar.xz
Source5920:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/synproof.tar.xz
Source5921:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/synproof.doc.tar.xz
Source6010:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shapes.tar.xz
Source6011:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shapes.doc.tar.xz
Source6013:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/slideshow.tar.xz
Source6014:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/slideshow.doc.tar.xz
Source6015:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/splines.tar.xz
Source6016:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/splines.doc.tar.xz
Source6018:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/suanpan.tar.xz
Source6019:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/suanpan.doc.tar.xz
Source6059:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/songbook.tar.xz
Source6060:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/songbook.doc.tar.xz
Source6062:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/songs.tar.xz
Source6063:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/songs.doc.tar.xz
Source6525:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/soton.tar.xz
Source6526:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/soton.doc.tar.xz
Source6527:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sphdthesis.tar.xz
Source6528:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sphdthesis.doc.tar.xz
Source6529:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spie.tar.xz
Source6530:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spie.doc.tar.xz
Source6531:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sr-vorl.tar.xz
Source6532:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sr-vorl.doc.tar.xz
Source6534:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stellenbosch.tar.xz
Source6535:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stellenbosch.doc.tar.xz
Source6537:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/suftesi.tar.xz
Source6538:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/suftesi.doc.tar.xz
Source6540:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sugconf.tar.xz
Source6541:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sugconf.doc.tar.xz
Source6722:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/siunitx.tar.xz
Source6723:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/siunitx.doc.tar.xz
Source6725:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/steinmetz.tar.xz
Source6726:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/steinmetz.doc.tar.xz
Source6728:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/struktex.tar.xz
Source6729:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/struktex.doc.tar.xz
Source6731:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/substances.tar.xz
Source6732:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/substances.doc.tar.xz
Source7505:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/signchart.tar.xz
Source7506:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/signchart.doc.tar.xz
Source7508:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simpler-wick.tar.xz
Source7509:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simpler-wick.doc.tar.xz
Source7510:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/smartunits.tar.xz
Source7511:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/smartunits.doc.tar.xz
Source7515:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svrsymbols.tar.xz
Source7516:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svrsymbols.doc.tar.xz
Source7945:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shobhika.tar.xz
Source7946:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/shobhika.doc.tar.xz
Source7947:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simple-resume-cv.tar.xz
Source7948:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simple-resume-cv.doc.tar.xz
Source7949:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simple-thesis-dissertation.tar.xz
Source7950:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simple-thesis-dissertation.doc.tar.xz
Source7951:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/soup.tar.xz
Source7952:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/soup.doc.tar.xz
Source7953:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spark-otf.tar.xz
Source7954:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spark-otf.doc.tar.xz
Source7955:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spectralsequences.tar.xz
Source7956:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spectralsequences.doc.tar.xz
Source7957:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/studenthandouts.tar.xz
Source7958:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/studenthandouts.doc.tar.xz
Source8046:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simplekv.doc.tar.xz
Source8047:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simplekv.tar.xz
Source8310:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/short-math-guide.tar.xz
Source8311:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/short-math-guide.doc.tar.xz
Source8312:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simpleinvoice.tar.xz
Source8313:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/simpleinvoice.doc.tar.xz
Source8314:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spalign.tar.xz
Source8315:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/spalign.doc.tar.xz
Source8316:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stanli.tar.xz
Source8317:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stanli.doc.tar.xz
Source8318:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statistics.tar.xz
Source8319:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statistics.doc.tar.xz
Source8322:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statmath.tar.xz
Source8323:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/statmath.doc.tar.xz
Source8324:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stealcaps.tar.xz
Source8325:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stealcaps.doc.tar.xz
Source8326:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stickstoo.tar.xz
Source8327:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stickstoo.doc.tar.xz
Source8328:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stix2-otf.tar.xz
Source8329:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stix2-otf.doc.tar.xz
Source8330:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stix2-type1.tar.xz
Source8331:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/stix2-type1.doc.tar.xz
Source8332:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/structmech.tar.xz
Source8333:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/structmech.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-showtags
Provides:       tex-showtags = %{tl_version}
License:        Public Domain
Summary:        Print the tags of bibliography entries
Version:        svn20336.1.05

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(showtags.sty) = %{tl_version}

%description -n texlive-showtags
Prints the tag right-aligned on each line of the bibliography.

%package -n texlive-showtags-doc
Summary:        Documentation for showtags
Version:        svn20336.1.05

Provides:       tex-showtags-doc
AutoReqProv:    No

%description -n texlive-showtags-doc
Documentation for showtags

%package -n texlive-sort-by-letters
Provides:       tex-sort-by-letters = %{tl_version}
License:        Bibtex
Summary:        Bibliography styles for alphabetic sorting
Version:        svn27128.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-sort-by-letters
This bundle contains several bibliography styles for separating
a document's references by the first letter of the first
author/editor in the bibliography entry. The styles are adapted
from standard ones or from natbib ones.

%package -n texlive-sort-by-letters-doc
Summary:        Documentation for sort-by-letters
Version:        svn27128.0

Provides:       tex-sort-by-letters-doc
AutoReqProv:    No

%description -n texlive-sort-by-letters-doc
Documentation for sort-by-letters

%package -n texlive-splitbib
Provides:       tex-splitbib = %{tl_version}
License:        LPPL
Summary:        Split and reorder your bibliography
Version:        svn15878.1.17

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(splitbib.sty) = %{tl_version}

%description -n texlive-splitbib
This package enables you to split a bibliography into several
categories and subcategories. It does not depend on BibTeX: any
bibliography may be split and reordered.

%package -n texlive-splitbib-doc
Summary:        Documentation for splitbib
Version:        svn15878.1.17

Provides:       tex-splitbib-doc
AutoReqProv:    No

%description -n texlive-splitbib-doc
Documentation for splitbib

%package -n texlive-stmaryrd
Provides:       tex-stmaryrd = %{tl_version}
License:        LPPL
Summary:        St Mary Road symbols for theoretical computer science
Version:        svn22027.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(stmaryrd.map) = %{tl_version}, tex(stmary10.tfm) = %{tl_version}
Provides:       tex(stmary5.tfm) = %{tl_version}, tex(stmary6.tfm) = %{tl_version}
Provides:       tex(stmary7.tfm) = %{tl_version}, tex(stmary8.tfm) = %{tl_version}
Provides:       tex(stmary9.tfm) = %{tl_version}, tex(stmary10.pfb) = %{tl_version}
Provides:       tex(stmary5.pfb) = %{tl_version}, tex(stmary6.pfb) = %{tl_version}
Provides:       tex(stmary7.pfb) = %{tl_version}, tex(stmary8.pfb) = %{tl_version}
Provides:       tex(stmary9.pfb) = %{tl_version}, tex(Ustmry.fd) = %{tl_version}
Provides:       tex(stmaryrd.sty) = %{tl_version}

%description -n texlive-stmaryrd
The fonts were originally distributed as Metafont sources only,
but Adobe Type 1 versions are also now available. Macro support
is provided for use under LaTeX; the package supports the
"only" option (provided by the somedefs package) to restrict
what is loaded, for those who don't need the whole font.

%package -n texlive-stmaryrd-doc
Summary:        Documentation for stmaryrd
Version:        svn22027.0

Provides:       tex-stmaryrd-doc
AutoReqProv:    No

%description -n texlive-stmaryrd-doc
Documentation for stmaryrd


%package -n texlive-skaknew
Provides:       tex-skaknew = %{tl_version}
License:        LPPL
Summary:        The skak chess fonts redone in Adobe Type 1
Version:        svn20031.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(SkakNew.map) = %{tl_version}, tex(AlphaDia.otf) = %{tl_version}
Provides:       tex(SkakNew-Diagram.otf) = %{tl_version}
Provides:       tex(SkakNew-DiagramT.otf) = %{tl_version}
Provides:       tex(SkakNew-Figurine.otf) = %{tl_version}
Provides:       tex(SkakNew-FigurineBold.otf) = %{tl_version}
Provides:       tex(AlphaDia.tfm) = %{tl_version}, tex(SkakNew-Diagram.tfm) = %{tl_version}
Provides:       tex(SkakNew-DiagramT.tfm) = %{tl_version}
Provides:       tex(SkakNew-Figurine.tfm) = %{tl_version}
Provides:       tex(SkakNew-FigurineBold.tfm) = %{tl_version}
Provides:       tex(AlphaDia.pfb) = %{tl_version}, tex(SkakNew-Diagram.pfb) = %{tl_version}
Provides:       tex(SkakNew-DiagramT.pfb) = %{tl_version}
Provides:       tex(SkakNew-Figurine.pfb) = %{tl_version}
Provides:       tex(SkakNew-FigurineBold.pfb) = %{tl_version}

%description -n texlive-skaknew
This package offers Adobe Type 1 versions of the fonts provided
as Metafont source by the skak bundle.

%package -n texlive-skaknew-doc
Summary:        Documentation for skaknew
Version:        svn20031.0

Provides:       tex-skaknew-doc
AutoReqProv:    No

%description -n texlive-skaknew-doc
Documentation for skaknew

%package -n texlive-skull
Provides:       tex-skull = %{tl_version}
License:        GPL+
Summary:        A font to draw a skull
Version:        svn25608.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(skull.sty) = %{tl_version}

%description -n texlive-skull
The font (defined in Metafont) defines a single character, a
black solid skull. A package is supplied to make this character
available as a symbol in maths mode.

%package -n texlive-sourcecodepro
Provides:       tex-sourcecodepro = %{tl_version}
License:        OFL
Summary:        Use SourceCodePro with TeX(-alike) systems
Version:        svn40597

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(fontenc.sty), tex(textcomp.sty), tex(mweights.sty), tex(fontaxes.sty)
Requires:       tex(xkeyval.sty), tex(ifxetex.sty), tex(ifluatex.sty), tex(fontspec.sty)
Provides:       tex(a_27avc7.enc) = %{tl_version}, tex(a_4t223s.enc) = %{tl_version}
Provides:       tex(a_6zrzoz.enc) = %{tl_version}, tex(a_7ovpxh.enc) = %{tl_version}
Provides:       tex(a_aoc6c2.enc) = %{tl_version}, tex(a_bldrys.enc) = %{tl_version}
Provides:       tex(a_djdyjq.enc) = %{tl_version}, tex(a_dz5hhp.enc) = %{tl_version}
Provides:       tex(a_gu5xou.enc) = %{tl_version}, tex(a_jvslvy.enc) = %{tl_version}
Provides:       tex(a_kinvs5.enc) = %{tl_version}, tex(a_ktd5xr.enc) = %{tl_version}
Provides:       tex(a_mqb3sg.enc) = %{tl_version}, tex(a_nkmn5f.enc) = %{tl_version}
Provides:       tex(a_omr5qy.enc) = %{tl_version}, tex(a_retzg2.enc) = %{tl_version}
Provides:       tex(a_s37xrq.enc) = %{tl_version}, tex(a_ubfwpl.enc) = %{tl_version}
Provides:       tex(a_xftsmg.enc) = %{tl_version}, tex(SourceCodePro.map) = %{tl_version}
Provides:       tex(SourceCodePro-Black.otf) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt.otf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold.otf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt.otf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight.otf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt.otf) = %{tl_version}
Provides:       tex(SourceCodePro-Light.otf) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt.otf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium.otf) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt.otf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular.otf) = %{tl_version}
Provides:       tex(SourceCodePro-RegularIt.otf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold.otf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt.otf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceCodePro-Black.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-Bold.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-It.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-Light.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-Medium.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-Regular.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt.pfb) = %{tl_version}
Provides:       tex(SourceCodePro-Black-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BlackIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-BoldIt-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLight-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-ExtraLightIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-It-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-LightIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-MediumIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-Semibold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceCodePro-SemiboldIt-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1SourceCodePro-Dnom.fd) = %{tl_version}
Provides:       tex(LY1SourceCodePro-Inf.fd) = %{tl_version}
Provides:       tex(LY1SourceCodePro-Numr.fd) = %{tl_version}
Provides:       tex(LY1SourceCodePro-Sup.fd) = %{tl_version}
Provides:       tex(LY1SourceCodePro-TLF.fd) = %{tl_version}
Provides:       tex(LY1SourceCodePro-TOsF.fd) = %{tl_version}
Provides:       tex(OT1SourceCodePro-Dnom.fd) = %{tl_version}
Provides:       tex(OT1SourceCodePro-Inf.fd) = %{tl_version}
Provides:       tex(OT1SourceCodePro-Numr.fd) = %{tl_version}
Provides:       tex(OT1SourceCodePro-Sup.fd) = %{tl_version}
Provides:       tex(OT1SourceCodePro-TLF.fd) = %{tl_version}
Provides:       tex(OT1SourceCodePro-TOsF.fd) = %{tl_version}
Provides:       tex(T1SourceCodePro-Dnom.fd) = %{tl_version}
Provides:       tex(T1SourceCodePro-Inf.fd) = %{tl_version}
Provides:       tex(T1SourceCodePro-Numr.fd) = %{tl_version}
Provides:       tex(T1SourceCodePro-Sup.fd) = %{tl_version}
Provides:       tex(T1SourceCodePro-TLF.fd) = %{tl_version}
Provides:       tex(T1SourceCodePro-TOsF.fd) = %{tl_version}
Provides:       tex(TS1SourceCodePro-TLF.fd) = %{tl_version}
Provides:       tex(TS1SourceCodePro-TOsF.fd) = %{tl_version}
Provides:       tex(sourcecodepro-type1-autoinst.sty) = %{tl_version}
Provides:       tex(SourceCodePro.sty) = %{tl_version}, tex(sourcecodepro.sty) = %{tl_version}

%description -n texlive-sourcecodepro
The font is an open-source Monospaced development from Adobe.
The package provides fonts (in both Adobe Type 1 and OpenType
formats) and macros supporting their use in LaTeX (Type 1) and
XeLaTeX/LuaLaTeX (OTF).

%package -n texlive-sourcecodepro-doc
Summary:        Documentation for sourcecodepro
Version:        svn40597

Provides:       tex-sourcecodepro-doc
AutoReqProv:    No

%description -n texlive-sourcecodepro-doc
Documentation for sourcecodepro

%package -n texlive-sourcesanspro
Provides:       tex-sourcesanspro = %{tl_version}
License:        OFL
Summary:        Use SourceSansPro with TeX(-alike) systems
Version:        svn42852
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(fontenc.sty)
Requires:       tex(textcomp.sty), tex(mweights.sty), tex(fontaxes.sty), tex(xkeyval.sty)
Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(fontspec.sty)
Provides:       tex(a_2cvp4u.enc) = %{tl_version}, tex(a_2jmt2m.enc) = %{tl_version}
Provides:       tex(a_2n3jyq.enc) = %{tl_version}, tex(a_3rlax2.enc) = %{tl_version}
Provides:       tex(a_3vq5rq.enc) = %{tl_version}, tex(a_4jf6oe.enc) = %{tl_version}
Provides:       tex(a_5mnkjz.enc) = %{tl_version}, tex(a_5tbsmu.enc) = %{tl_version}
Provides:       tex(a_6bttxp.enc) = %{tl_version}, tex(a_b457hn.enc) = %{tl_version}
Provides:       tex(a_cvynlr.enc) = %{tl_version}, tex(a_cxftuq.enc) = %{tl_version}
Provides:       tex(a_debg3j.enc) = %{tl_version}, tex(a_el7rh7.enc) = %{tl_version}
Provides:       tex(a_elrf5h.enc) = %{tl_version}, tex(a_ev2kyj.enc) = %{tl_version}
Provides:       tex(a_floqlo.enc) = %{tl_version}, tex(a_fva737.enc) = %{tl_version}
Provides:       tex(a_gc2pqo.enc) = %{tl_version}, tex(a_ggs4wk.enc) = %{tl_version}
Provides:       tex(a_gsofwu.enc) = %{tl_version}, tex(a_gw3vm7.enc) = %{tl_version}
Provides:       tex(a_ifkpwm.enc) = %{tl_version}, tex(a_j24bgz.enc) = %{tl_version}
Provides:       tex(a_jpwolx.enc) = %{tl_version}, tex(a_kksgzp.enc) = %{tl_version}
Provides:       tex(a_ko3vnf.enc) = %{tl_version}, tex(a_mhce32.enc) = %{tl_version}
Provides:       tex(a_myad3x.enc) = %{tl_version}, tex(a_n5gv3r.enc) = %{tl_version}
Provides:       tex(a_n5mfkj.enc) = %{tl_version}, tex(a_nlm4w5.enc) = %{tl_version}
Provides:       tex(a_p5cgg3.enc) = %{tl_version}, tex(a_pcov5a.enc) = %{tl_version}
Provides:       tex(a_psnyba.enc) = %{tl_version}, tex(a_qujrng.enc) = %{tl_version}
Provides:       tex(a_r6twhl.enc) = %{tl_version}, tex(a_rsnzt5.enc) = %{tl_version}
Provides:       tex(a_sd7igg.enc) = %{tl_version}, tex(a_tczf5d.enc) = %{tl_version}
Provides:       tex(a_tophx4.enc) = %{tl_version}, tex(a_tzjlps.enc) = %{tl_version}
Provides:       tex(a_umlpmm.enc) = %{tl_version}, tex(a_v4sjy4.enc) = %{tl_version}
Provides:       tex(a_v537dd.enc) = %{tl_version}, tex(a_vx5ywn.enc) = %{tl_version}
Provides:       tex(a_w2dgod.enc) = %{tl_version}, tex(a_x5hjjp.enc) = %{tl_version}
Provides:       tex(a_xfkmtv.enc) = %{tl_version}, tex(a_yugc2g.enc) = %{tl_version}
Provides:       tex(SourceSansPro.map) = %{tl_version}, tex(SourceSansPro-Black.otf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt.otf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold.otf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt.otf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight.otf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt.otf) = %{tl_version}
Provides:       tex(SourceSansPro-Light.otf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt.otf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular.otf) = %{tl_version}
Provides:       tex(SourceSansPro-RegularIt.otf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold.otf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt.otf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSansPro-Black.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-Bold.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-It.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-Light.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-Regular.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt.pfb) = %{tl_version}
Provides:       tex(SourceSansPro-Black-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BlackIt-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-BoldIt-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLight-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-ExtraLightIt-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-It-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-LightIt-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-Semibold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSansPro-SemiboldIt-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1SourceSansPro-Dnom.fd) = %{tl_version}
Provides:       tex(LY1SourceSansPro-Inf.fd) = %{tl_version}
Provides:       tex(LY1SourceSansPro-LF.fd) = %{tl_version}
Provides:       tex(LY1SourceSansPro-Numr.fd) = %{tl_version}
Provides:       tex(LY1SourceSansPro-OsF.fd) = %{tl_version}
Provides:       tex(LY1SourceSansPro-Sup.fd) = %{tl_version}
Provides:       tex(LY1SourceSansPro-TLF.fd) = %{tl_version}
Provides:       tex(LY1SourceSansPro-TOsF.fd) = %{tl_version}
Provides:       tex(OT1SourceSansPro-Dnom.fd) = %{tl_version}
Provides:       tex(OT1SourceSansPro-Inf.fd) = %{tl_version}
Provides:       tex(OT1SourceSansPro-LF.fd) = %{tl_version}
Provides:       tex(OT1SourceSansPro-Numr.fd) = %{tl_version}
Provides:       tex(OT1SourceSansPro-OsF.fd) = %{tl_version}
Provides:       tex(OT1SourceSansPro-Sup.fd) = %{tl_version}
Provides:       tex(OT1SourceSansPro-TLF.fd) = %{tl_version}
Provides:       tex(OT1SourceSansPro-TOsF.fd) = %{tl_version}
Provides:       tex(T1SourceSansPro-Dnom.fd) = %{tl_version}
Provides:       tex(T1SourceSansPro-Inf.fd) = %{tl_version}
Provides:       tex(T1SourceSansPro-LF.fd) = %{tl_version}
Provides:       tex(T1SourceSansPro-Numr.fd) = %{tl_version}
Provides:       tex(T1SourceSansPro-OsF.fd) = %{tl_version}
Provides:       tex(T1SourceSansPro-Sup.fd) = %{tl_version}
Provides:       tex(T1SourceSansPro-TLF.fd) = %{tl_version}
Provides:       tex(T1SourceSansPro-TOsF.fd) = %{tl_version}
Provides:       tex(TS1SourceSansPro-LF.fd) = %{tl_version}
Provides:       tex(TS1SourceSansPro-OsF.fd) = %{tl_version}
Provides:       tex(TS1SourceSansPro-TLF.fd) = %{tl_version}
Provides:       tex(TS1SourceSansPro-TOsF.fd) = %{tl_version}
Provides:       tex(sourcesanspro-type1-autoinst.sty) = %{tl_version}
Provides:       tex(SourceSansPro.sty) = %{tl_version}, tex(sourcesanspro.sty) = %{tl_version}

%description -n texlive-sourcesanspro
The font is an open-source Sans-Serif development from Adobe.
The package provides fonts (in both Adobe Type 1 and OpenType
formats) and macros supporting their use in LaTeX (Type 1) and
XeLaTeX/LuaLaTeX (OTF).

%package -n texlive-sourcesanspro-doc
Summary:        Documentation for sourcesanspro
Version:        svn42852
Provides:       tex-sourcesanspro-doc
AutoReqProv:    No

%description -n texlive-sourcesanspro-doc
Documentation for sourcesanspro

%package -n texlive-sourceserifpro
Provides:       tex-sourceserifpro = %{tl_version}
License:        OFL
Summary:        Use SourceSerifPro with TeX(-alike) systems
Version:        svn40598

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(fontenc.sty), tex(textcomp.sty), tex(mweights.sty), tex(fontaxes.sty)
Requires:       tex(xkeyval.sty), tex(ifxetex.sty), tex(ifluatex.sty), tex(fontspec.sty)
Provides:       tex(a_3gun5d.enc) = %{tl_version}, tex(a_64kcwv.enc) = %{tl_version}
Provides:       tex(a_7c323s.enc) = %{tl_version}, tex(a_7vfhsm.enc) = %{tl_version}
Provides:       tex(a_a5mxzo.enc) = %{tl_version}, tex(a_c5lvge.enc) = %{tl_version}
Provides:       tex(a_c6mgd7.enc) = %{tl_version}, tex(a_cx2wj7.enc) = %{tl_version}
Provides:       tex(a_fv7osb.enc) = %{tl_version}, tex(a_iem7z5.enc) = %{tl_version}
Provides:       tex(a_kuzlbp.enc) = %{tl_version}, tex(a_mtsjm5.enc) = %{tl_version}
Provides:       tex(a_n5wndz.enc) = %{tl_version}, tex(a_oim3qx.enc) = %{tl_version}
Provides:       tex(a_owk7oj.enc) = %{tl_version}, tex(a_pvm6tr.enc) = %{tl_version}
Provides:       tex(a_r5qp3q.enc) = %{tl_version}, tex(a_rgwjxa.enc) = %{tl_version}
Provides:       tex(a_rsqbul.enc) = %{tl_version}, tex(a_sxytol.enc) = %{tl_version}
Provides:       tex(a_t4jhwy.enc) = %{tl_version}, tex(a_ttcihk.enc) = %{tl_version}
Provides:       tex(a_vj4et7.enc) = %{tl_version}, tex(a_vz2niz.enc) = %{tl_version}
Provides:       tex(a_yds5jv.enc) = %{tl_version}, tex(SourceSerifPro.map) = %{tl_version}
Provides:       tex(SourceSerifPro-Black.otf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold.otf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight.otf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light.otf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular.otf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold.otf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ot1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SourceSerifPro-Black.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-BlackLCDFJ.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLightLCDFJ.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-Light.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-LightLCDFJ.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-RegularLCDFJ.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-SemiboldLCDFJ.pfb) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Black-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-ExtraLight-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-dnom-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-inf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-lf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-numr-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-osf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-sup-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ot1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-t1.vf) = %{tl_version}
Provides:       tex(SourceSerifPro-Semibold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1SourceSerifPro-Dnom.fd) = %{tl_version}
Provides:       tex(LY1SourceSerifPro-Inf.fd) = %{tl_version}
Provides:       tex(LY1SourceSerifPro-LF.fd) = %{tl_version}
Provides:       tex(LY1SourceSerifPro-Numr.fd) = %{tl_version}
Provides:       tex(LY1SourceSerifPro-OsF.fd) = %{tl_version}
Provides:       tex(LY1SourceSerifPro-Sup.fd) = %{tl_version}
Provides:       tex(LY1SourceSerifPro-TLF.fd) = %{tl_version}
Provides:       tex(LY1SourceSerifPro-TOsF.fd) = %{tl_version}
Provides:       tex(OT1SourceSerifPro-Dnom.fd) = %{tl_version}
Provides:       tex(OT1SourceSerifPro-Inf.fd) = %{tl_version}
Provides:       tex(OT1SourceSerifPro-LF.fd) = %{tl_version}
Provides:       tex(OT1SourceSerifPro-Numr.fd) = %{tl_version}
Provides:       tex(OT1SourceSerifPro-OsF.fd) = %{tl_version}
Provides:       tex(OT1SourceSerifPro-Sup.fd) = %{tl_version}
Provides:       tex(OT1SourceSerifPro-TLF.fd) = %{tl_version}
Provides:       tex(OT1SourceSerifPro-TOsF.fd) = %{tl_version}
Provides:       tex(T1SourceSerifPro-Dnom.fd) = %{tl_version}
Provides:       tex(T1SourceSerifPro-Inf.fd) = %{tl_version}
Provides:       tex(T1SourceSerifPro-LF.fd) = %{tl_version}
Provides:       tex(T1SourceSerifPro-Numr.fd) = %{tl_version}
Provides:       tex(T1SourceSerifPro-OsF.fd) = %{tl_version}
Provides:       tex(T1SourceSerifPro-Sup.fd) = %{tl_version}
Provides:       tex(T1SourceSerifPro-TLF.fd) = %{tl_version}
Provides:       tex(T1SourceSerifPro-TOsF.fd) = %{tl_version}
Provides:       tex(TS1SourceSerifPro-LF.fd) = %{tl_version}
Provides:       tex(TS1SourceSerifPro-OsF.fd) = %{tl_version}
Provides:       tex(TS1SourceSerifPro-TLF.fd) = %{tl_version}
Provides:       tex(TS1SourceSerifPro-TOsF.fd) = %{tl_version}
Provides:       tex(sourceserifpro-type1-autoinst.sty) = %{tl_version}
Provides:       tex(SourceSerifPro.sty) = %{tl_version}, tex(sourceserifpro.sty) = %{tl_version}

%description -n texlive-sourceserifpro
This package provides Source Serif Pro for LaTeX. It includes
both Type1 and OpenType fonts and selects the latter when using
XeLaTeX or LuaLaTeX. Issues with this package can be reported
on GitHub (https://github.com/silkeh/latex-
sourceserifpro/issues) or emailed to tex@slxh.nl.

%package -n texlive-sourceserifpro-doc
Summary:        Documentation for sourceserifpro
Version:        svn40598

Provides:       tex-sourceserifpro-doc
AutoReqProv:    No

%description -n texlive-sourceserifpro-doc
Documentation for sourceserifpro

%package -n texlive-sides
Provides:       tex-sides = %{tl_version}
License:        GPL+
Summary:        A LaTeX class for typesetting stage plays
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sides.cls) = %{tl_version}

%description -n texlive-sides
This is a LaTeX class for typesetting stage plays, based on the
plari class written by Antti-Juhani Kaijanaho in 1998. It has
been updated and several formatting changes have been made to
it--most noticibly there are no longer orphans.

%package -n texlive-sides-doc
Summary:        Documentation for sides
Version:        svn15878.0

Provides:       tex-sides-doc
AutoReqProv:    No

%description -n texlive-sides-doc
Documentation for sides

%package -n texlive-stage
Provides:       tex-stage = %{tl_version}
License:        LPPL 1.3
Summary:        A LaTeX class for stage plays
Version:        svn44100
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(fancyhdr.sty), tex(extramarks.sty)
Provides:       tex(stage.cls) = %{tl_version}

%description -n texlive-stage
Stage.cls is a LaTeX class for creating plays of any length in
a standard manuscript format for production and submission.

%package -n texlive-stage-doc
Summary:        Documentation for stage
Version:        svn44100
Provides:       tex-stage-doc
AutoReqProv:    No

%description -n texlive-stage-doc
Documentation for stage

%package -n texlive-starfont
Provides:       tex-starfont = %{tl_version}
License:        Public Domain
Summary:        The StarFont Sans astrological font
Version:        svn19982.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(starfont.map) = %{tl_version}, tex(fstr8x.tfm) = %{tl_version}
Provides:       tex(fsts8x.tfm) = %{tl_version}, tex(starfont.pfb) = %{tl_version}
Provides:       tex(strfnser.pfb) = %{tl_version}, tex(starfont.sty) = %{tl_version}

%description -n texlive-starfont
The package contains StarFontSans and StarFontSerif, two public-
domain astrological fonts designed by Anthony I.P. Owen, and
the appropriate macros to use them with TeX and LaTeX. The
fonts are supplied both in the original TrueType Format and in
Adobe Type 1 format.

%package -n texlive-starfont-doc
Summary:        Documentation for starfont
Version:        svn19982.1.2

Provides:       tex-starfont-doc
AutoReqProv:    No

%description -n texlive-starfont-doc
Documentation for starfont

%package -n texlive-staves
Provides:       tex-staves = %{tl_version}
License:        LPPL
Summary:        Typeset Icelandic staves and runic letters
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(icelandic.map) = %{tl_version}, tex(icelandic.tfm) = %{tl_version}
Provides:       tex(icelandic.pfb) = %{tl_version}, tex(staves.sty) = %{tl_version}

%description -n texlive-staves
This package contains all the necessary tools to typeset the
"magical" Icelandic staves plus the runic letters used in
Iceland. Included are a font in Adobe Type 1 format and LaTeX
support.

%package -n texlive-staves-doc
Summary:        Documentation for staves
Version:        svn15878.0

Provides:       tex-staves-doc
AutoReqProv:    No

%description -n texlive-staves-doc
Documentation for staves

%package -n texlive-stix
Provides:       tex-stix = %{tl_version}
License:        OFL
Summary:        OpenType Unicode maths fonts
Version:        svn47652
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(textcomp.sty)
Requires:       stix-fonts stix-math-fonts
Provides:       tex(stix-extra1.enc) = %{tl_version}, tex(stix-extra2.enc) = %{tl_version}
Provides:       tex(stix-extra3.enc) = %{tl_version}, tex(stix-ot1.enc) = %{tl_version}
Provides:       tex(stix-ot2.enc) = %{tl_version}, tex(stix-t1.enc) = %{tl_version}
Provides:       tex(stix-ts1.enc) = %{tl_version}, tex(stix.map) = %{tl_version}
Provides:       tex(STIX-Bold.otf) = %{tl_version}, tex(STIX-BoldItalic.otf) = %{tl_version}
Provides:       tex(STIX-Italic.otf) = %{tl_version}, tex(STIX-Regular.otf) = %{tl_version}
Provides:       tex(STIXMath-Regular.otf) = %{tl_version}
Provides:       tex(ot1-stixgeneralsc-bold.vpl) = %{tl_version}
Provides:       tex(ot1-stixgeneralsc.vpl) = %{tl_version}
Provides:       tex(ot2-stixgeneralsc-bold.vpl) = %{tl_version}
Provides:       tex(ot2-stixgeneralsc.vpl) = %{tl_version}
Provides:       tex(t1-stixgeneralsc-bold.vpl) = %{tl_version}
Provides:       tex(t1-stixgeneralsc.vpl) = %{tl_version}
Provides:       tex(ot1-stixgeneral-bold.tfm) = %{tl_version}
Provides:       tex(ot1-stixgeneral-bolditalic.tfm) = %{tl_version}
Provides:       tex(ot1-stixgeneral-italic.tfm) = %{tl_version}
Provides:       tex(ot1-stixgeneral.tfm) = %{tl_version}
Provides:       tex(ot1-stixgeneralsc-bold.tfm) = %{tl_version}
Provides:       tex(ot1-stixgeneralsc.tfm) = %{tl_version}
Provides:       tex(ot2-stixgeneral-bold.tfm) = %{tl_version}
Provides:       tex(ot2-stixgeneral-bolditalic.tfm) = %{tl_version}
Provides:       tex(ot2-stixgeneral-italic.tfm) = %{tl_version}
Provides:       tex(ot2-stixgeneral.tfm) = %{tl_version}
Provides:       tex(ot2-stixgeneralsc-bold.tfm) = %{tl_version}
Provides:       tex(ot2-stixgeneralsc.tfm) = %{tl_version}
Provides:       tex(stix-extra1.tfm) = %{tl_version}, tex(stix-extra2.tfm) = %{tl_version}
Provides:       tex(stix-extra3.tfm) = %{tl_version}, tex(stix-mathbb-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathbb.tfm) = %{tl_version}, tex(stix-mathbbit-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathbbit.tfm) = %{tl_version}, tex(stix-mathcal-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathcal.tfm) = %{tl_version}, tex(stix-mathex-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathex.tfm) = %{tl_version}, tex(stix-mathfrak-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathfrak.tfm) = %{tl_version}, tex(stix-mathit-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathit.tfm) = %{tl_version}, tex(stix-mathrm-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathrm.tfm) = %{tl_version}, tex(stix-mathscr-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathscr.tfm) = %{tl_version}, tex(stix-mathsf-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathsf.tfm) = %{tl_version}, tex(stix-mathsfit-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathsfit.tfm) = %{tl_version}, tex(stix-mathtt-bold.tfm) = %{tl_version}
Provides:       tex(stix-mathtt.tfm) = %{tl_version}, tex(t1-stixgeneral-bold.tfm) = %{tl_version}
Provides:       tex(t1-stixgeneral-bolditalic.tfm) = %{tl_version}
Provides:       tex(t1-stixgeneral-italic.tfm) = %{tl_version}
Provides:       tex(t1-stixgeneral.tfm) = %{tl_version}, tex(t1-stixgeneralsc-bold.tfm) = %{tl_version}
Provides:       tex(t1-stixgeneralsc.tfm) = %{tl_version}
Provides:       tex(ts1-stixgeneral-bold.tfm) = %{tl_version}
Provides:       tex(ts1-stixgeneral-bolditalic.tfm) = %{tl_version}
Provides:       tex(ts1-stixgeneral-italic.tfm) = %{tl_version}
Provides:       tex(ts1-stixgeneral.tfm) = %{tl_version}
Provides:       tex(STIXGeneral-Bold.pfb) = %{tl_version}
Provides:       tex(STIXGeneral-BoldItalic.pfb) = %{tl_version}
Provides:       tex(STIXGeneral-Italic.pfb) = %{tl_version}
Provides:       tex(STIXGeneral-Regular.pfb) = %{tl_version}
Provides:       tex(stix-mathbb-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathbb.pfb) = %{tl_version}, tex(stix-mathbbit-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathbbit.pfb) = %{tl_version}, tex(stix-mathcal-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathcal.pfb) = %{tl_version}, tex(stix-mathex-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathex.pfb) = %{tl_version}, tex(stix-mathfrak-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathfrak.pfb) = %{tl_version}, tex(stix-mathit-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathit.pfb) = %{tl_version}, tex(stix-mathrm-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathrm.pfb) = %{tl_version}, tex(stix-mathscr-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathscr.pfb) = %{tl_version}, tex(stix-mathsf-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathsf.pfb) = %{tl_version}, tex(stix-mathsfit-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathsfit.pfb) = %{tl_version}, tex(stix-mathtt-bold.pfb) = %{tl_version}
Provides:       tex(stix-mathtt.pfb) = %{tl_version}, tex(ot1-stixgeneralsc-bold.vf) = %{tl_version}
Provides:       tex(ot1-stixgeneralsc.vf) = %{tl_version}
Provides:       tex(ot2-stixgeneralsc-bold.vf) = %{tl_version}
Provides:       tex(ot2-stixgeneralsc.vf) = %{tl_version}
Provides:       tex(t1-stixgeneralsc-bold.vf) = %{tl_version}
Provides:       tex(t1-stixgeneralsc.vf) = %{tl_version}
Provides:       tex(ls1stix.fd) = %{tl_version}, tex(ls1stixbb.fd) = %{tl_version}
Provides:       tex(ls1stixfrak.fd) = %{tl_version}, tex(ls1stixscr.fd) = %{tl_version}
Provides:       tex(ls1stixsf.fd) = %{tl_version}, tex(ls2stix.fd) = %{tl_version}
Provides:       tex(ls2stixcal.fd) = %{tl_version}, tex(ls2stixex.fd) = %{tl_version}
Provides:       tex(ls2stixtt.fd) = %{tl_version}, tex(ot1stix.fd) = %{tl_version}
Provides:       tex(ot2stix.fd) = %{tl_version}, tex(stix.sty) = %{tl_version}
Provides:       tex(t1stix.fd) = %{tl_version}, tex(ts1stix.fd) = %{tl_version}

%description -n texlive-stix
The STIX fonts are a suite of unicode OpenType fonts containing
a complete set of mathematical glyphs. The CTAN package is a
copy of the fonts' official release, organised as specified by
the TeX Directory Structure, for inclusion in standard TeX
distributions. A Type 1-only distribution of the fonts is
available in the esstix bundle.

%package -n texlive-stix-doc
Summary:        Documentation for stix
Version:        svn47652
Provides:       tex-stix-doc
AutoReqProv:    No

%description -n texlive-stix-doc
Documentation for stix

%package -n texlive-superiors
Provides:       tex-superiors = %{tl_version}
License:        LPPL
Summary:        Attach superior figures to a font family
Version:        svn36422.1.05

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty), tex(pgffor.sty)
Provides:       tex(sups.enc) = %{tl_version}, tex(superiors.map) = %{tl_version}
Provides:       tex(libertinesups.tfm) = %{tl_version}, tex(libertinesups.pfb) = %{tl_version}
Provides:       tex(superiors.sty) = %{tl_version}

%description -n texlive-superiors
The package allows the attachment of an arbitrary superior
figures font to a font family that lacks one. (Superior figures
are commonly used as footnote markers.) Two superior figures
fonts are provided--one matching Times, the other matching
Libertine.

%package -n texlive-superiors-doc
Summary:        Documentation for superiors
Version:        svn36422.1.05

Provides:       tex-superiors-doc
AutoReqProv:    No

%description -n texlive-superiors-doc
Documentation for superiors

%package -n texlive-symbol
Provides:       tex-symbol = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn31835.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(usy.map) = %{tl_version}, tex(psyr.tfm) = %{tl_version}
Provides:       tex(msyr.tfm) = %{tl_version}, tex(usyr.tfm) = %{tl_version}
Provides:       tex(usyr.pfb) = %{tl_version}, tex(uusy.fd) = %{tl_version}

%description -n texlive-symbol
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-startex
Provides:       tex-startex = %{tl_version}
License:        Public Domain
Summary:        An XML-inspired format for student use
Version:        svn35718.1.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(startex.tex) = %{tl_version}

%description -n texlive-startex
A TeX format designed to help students write short reports and
essays. It provides the user with a suitable set of commands
for such a task. It is also more robust than plain TeX and
LaTeX.

%package -n texlive-startex-doc
Summary:        Documentation for startex
Version:        svn35718.1.04

Provides:       tex-startex-doc
AutoReqProv:    No

%description -n texlive-startex-doc
Documentation for startex

%package -n texlive-skak
Provides:       tex-skak = %{tl_version}
License:        LPPL
Summary:        Fonts and macros for typesetting chess games
Version:        svn46259
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(latexsym.sty), tex(chessfss.sty), tex(lambda.sty), tex(ifthen.sty)
Requires:       tex(calc.sty), tex(textcomp.sty), tex(pstricks.sty), tex(pst-node.sty)
Provides:       tex(skak10.tfm) = %{tl_version}, tex(skak15.tfm) = %{tl_version}
Provides:       tex(skak20.tfm) = %{tl_version}, tex(skak30.tfm) = %{tl_version}
Provides:       tex(skakf10.tfm) = %{tl_version}, tex(skakf10b.tfm) = %{tl_version}
Provides:       tex(chess-workshop-symbols.sty) = %{tl_version}
Provides:       tex(skak.fd) = %{tl_version}, tex(skak.sty) = %{tl_version}
Provides:       tex(uskak.fd) = %{tl_version}

%description -n texlive-skak
This package provides macros and fonts in Metafont format which
can be used to typeset chess games using PGN, and to show
diagrams of the current board in a document. The package builds
on work by Piet Tutelaers -- the main novelty is the use of PGN
for input instead of the more cumbersome coordinate notation
(g1f3 becomes the more readable Nf3 in PGN). An Adobe Type 1
implementation of skak's fonts is available as package skaknew;
an alternative chess notational scheme is available in package
texmate, and a general mechanism for selecting chess fonts is
provided in chessfss.

%package -n texlive-skak-doc
Summary:        Documentation for skak
Version:        svn46259
Provides:       tex-skak-doc
AutoReqProv:    No

%description -n texlive-skak-doc
Documentation for skak

%package -n texlive-sudoku
Provides:       tex-sudoku = %{tl_version}
License:        LPPL
Summary:        Create sudoku grids
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sudoku.sty) = %{tl_version}

%description -n texlive-sudoku
The sudoku package provides an environment for typesetting
sudoku grids. A sudoku puzzle is a 9x9 grid where some of the
squares in the grid contain numbers. The rules are simple:
every column can only contain the digits 1 to 9, every row can
only contain the digits 1 to 9 and every 3x3 box can only
contain the digits 1 to 9. More information, including help and
example puzzles, can be found at sudoku.org.uk. This site also
has blank sudoku grids (or worksheets), but you will not need
to print them from there if you have this package installed.

%package -n texlive-sudoku-doc
Summary:        Documentation for sudoku
Version:        svn15878.1.0

Provides:       tex-sudoku-doc
AutoReqProv:    No

%description -n texlive-sudoku-doc
Documentation for sudoku

%package -n texlive-sudokubundle
Provides:       tex-sudokubundle = %{tl_version}
License:        LPPL
Summary:        A set of sudoku-related packages
Version:        svn15878.1.0a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(random.tex)
Provides:       tex(createsudoku.sty) = %{tl_version}, tex(printsudoku.sty) = %{tl_version}
Provides:       tex(solvesudoku.sty) = %{tl_version}

%description -n texlive-sudokubundle
The bundle provides three packages: printsudoku, which provides
a command \sudoku whose argument is the name of a file
containing a puzzle specification; solvesudoku, which attempts
to find a solution to the puzzle in the file named in the
argument; and createsudoku, which uses the random package to
generate a puzzle according to a bunch of parameters that the
user sets via macros. The bundle comes with a set of ready-
prepared puzzle files.

%package -n texlive-sudokubundle-doc
Summary:        Documentation for sudokubundle
Version:        svn15878.1.0a

Provides:       tex-sudokubundle-doc
AutoReqProv:    No

%description -n texlive-sudokubundle-doc
Documentation for sudokubundle

%package -n texlive-shade
Provides:       tex-shade = %{tl_version}
License:        LPPL
Summary:        Shade pieces of text
Version:        svn22212.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(shade.tex) = %{tl_version}

%description -n texlive-shade
The package provides a shaded backdrop to a box of text. It
uses a Metafont font (provided) which generates to appropriate
shading dependent on the resolution used in the Metafont
printer parameters.

%package -n texlive-shade-doc
Summary:        Documentation for shade
Version:        svn22212.1

Provides:       tex-shade-doc
AutoReqProv:    No

%description -n texlive-shade-doc
Documentation for shade

%package -n texlive-shapes
Provides:       tex-shapes = %{tl_version}
License:        LPPL 1.3
Summary:        Draw polygons, reentrant stars, and fractions in circles with Metapost
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-shapes
The shapes set of macros allows drawing regular polygons; their
corresponding reentrant stars in all their variations; and
fractionally filled circles (useful for visually demonstrating
the nature of fractions) in Metapost.

%package -n texlive-shapes-doc
Summary:        Documentation for shapes
Version:        svn42428
Provides:       tex-shapes-doc
AutoReqProv:    No

%description -n texlive-shapes-doc
Documentation for shapes

%package -n texlive-slideshow
Provides:       tex-slideshow = %{tl_version}
License:        Copyright only
Summary:        Generate slideshow with MetaPost
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-slideshow
The package provides a means of creating presentations in
MetaPost, without intervention from other utilities (except a
distiller). Such an arrangement has its advantages (though
there are disadvantages too).

%package -n texlive-slideshow-doc
Summary:        Documentation for slideshow
Version:        svn15878.1.0

Provides:       tex-slideshow-doc
AutoReqProv:    No

%description -n texlive-slideshow-doc
Documentation for slideshow

%package -n texlive-splines
Provides:       tex-splines = %{tl_version}
License:        LPPL 1.3
Summary:        MetaPost macros for drawing cubic spline interpolants
Version:        svn15878.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-splines
This is a small package of macros for creating cubic spline
interpolants in MetaPost or Metafont. Given a list of points
the macros can produce a closed or a relaxed spline joining
them. Given a list of function values y_j at x_j, the result
would define the graph of a cubic spline interpolating function
y=f(x), which is either periodic or relaxed.

%package -n texlive-splines-doc
Summary:        Documentation for splines
Version:        svn15878.0.2

Provides:       tex-splines-doc
AutoReqProv:    No

%description -n texlive-splines-doc
Documentation for splines

%package -n texlive-suanpan
Provides:       tex-suanpan = %{tl_version}
License:        LPPL
Summary:        MetaPost macros for drawing Chinese and Japanese abaci
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-suanpan
These macros are described in Denis Roegel: MetaPost macros for
drawing Chinese and Japanese abaci, TUGboat (volume 30, number
1, 2009, pages 74-79)

%package -n texlive-suanpan-doc
Summary:        Documentation for suanpan
Version:        svn15878.0

Provides:       tex-suanpan-doc
AutoReqProv:    No

%description -n texlive-suanpan-doc
Documentation for suanpan

%package -n texlive-systeme
Provides:       tex-systeme = %{tl_version}
License:        LPPL 1.3
Summary:        Format systems of equations
Version:        svn46184
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xstring.sty)
Provides:       tex(systeme.sty) = %{tl_version}, tex(systeme.tex) = %{tl_version}

%description -n texlive-systeme
The package allows you to enter systems of equations or
inequalities in an intuitive way, and produces typeset output
where the terms and signs are aligned vertically. The package
works with plain TeX or LaTeX, but e-TeX is required. Cette
petite extension permet de saisir des systemes d'equations ou
inequations de facon intuitive, et produit un affichage ou les
termes et les signes sont alignes verticalement.

%package -n texlive-systeme-doc
Summary:        Documentation for systeme
Version:        svn46184
Provides:       tex-systeme-doc
AutoReqProv:    No

%description -n texlive-systeme-doc
Documentation for systeme

%package -n texlive-subfig
Provides:       tex-subfig = %{tl_version}
License:        LPPL
Summary:        Figures broken into subfigures
Version:        svn15878.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(caption.sty), tex(caption3.sty)
Provides:       tex(altsf.cfg) = %{tl_version}, tex(subfig.sty) = %{tl_version}

%description -n texlive-subfig
The package provides support for the manipulation and reference
of small or 'sub' figures and tables within a single figure or
table environment. It is convenient to use this package when
your subfigures are to be separately captioned, referenced, or
are to be included in the List-of-Figures. A new \subfigure
command is introduced which can be used inside a figure
environment for each subfigure. An optional first argument is
used as the caption for that subfigure. This package supersedes
the subfigure package (which is no longer maintained). The name
was changed since the package is completely backward compatible
with the older package The major advantage to the new package
is that the user interface is keyword/value driven and easier
to use. To ease the transition from the subfigure package, the
distribution it includes a configuration file (subfig.cfg)
which nearly emulates the subfigure package. The functionality
of the package is provided by the (more recent still)
subcaption package.

%package -n texlive-subfig-doc
Summary:        Documentation for subfig
Version:        svn15878.1.3

Provides:       tex-subfig-doc
AutoReqProv:    No

%description -n texlive-subfig-doc
Documentation for subfig

%package -n texlive-shadethm
Provides:       tex-shadethm = %{tl_version}
License:        LPPL
Summary:        Theorem environments that are shaded
Version:        svn20319.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(shadethm.sty) = %{tl_version}

%description -n texlive-shadethm
Extends the \newtheorem command. If you say
\newshadetheorem{theorem}{Theorem} in the preamble then your
regular \begin{theorem} .. \end{theorem} will produce a theorem
statement in a shaded box. It supports all the options of
\newtheorem, including forms \newshadetheorem{..}[..]{..} and
\newshadetheorem{..}{..}[..]. Environments declared using the
package require their body to remain on one page; the mdframed
package can frame and shade theorems, and its environments
break at the end of a page; users are generally recommended,
therefore, to use mdframed.

%package -n texlive-shadethm-doc
Summary:        Documentation for shadethm
Version:        svn20319.0

Provides:       tex-shadethm-doc
AutoReqProv:    No

%description -n texlive-shadethm-doc
Documentation for shadethm

%package -n texlive-shadow
Provides:       tex-shadow = %{tl_version}
License:        LPPL
Summary:        Shadow boxes
Version:        svn20312.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(shadow.sty) = %{tl_version}

%description -n texlive-shadow
Defines a command \shabox (analgous to \fbox), and supporting
mechanisms.

%package -n texlive-shadow-doc
Summary:        Documentation for shadow
Version:        svn20312.0

Provides:       tex-shadow-doc
AutoReqProv:    No

%description -n texlive-shadow-doc
Documentation for shadow

%package -n texlive-shadowtext
Provides:       tex-shadowtext = %{tl_version}
License:        LPPL
Summary:        shadowtext
Version:        svn26522.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(shadowtext.sty) = %{tl_version}

%description -n texlive-shadowtext
The package introduces a command \shadowtext, which adds a drop
shadow to the text that is given as its argument. The colour
and positioning of the shadow are customisable.

%package -n texlive-shadowtext-doc
Summary:        Documentation for shadowtext
Version:        svn26522.0.3

Provides:       tex-shadowtext-doc
AutoReqProv:    No

%description -n texlive-shadowtext-doc
Documentation for shadowtext

%package -n texlive-shapepar
Provides:       tex-shapepar = %{tl_version}
License:        Dotseqn
Summary:        A macro to typeset paragraphs in specific shapes
Version:        svn30708.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(Canflagshape.def) = %{tl_version}, tex(TeXshape.def) = %{tl_version}
Provides:       tex(candleshape.def) = %{tl_version}, tex(dropshape.def) = %{tl_version}
Provides:       tex(shapepar.sty) = %{tl_version}, tex(triangleshapes.def) = %{tl_version}

%description -n texlive-shapepar
\shapepar is a macro to typeset paragraphs in a specific shape.
The size is adjusted automatically so that the entire shape is
filled with text. There may not be displayed maths or
'\vadjust' material (no \vspace) in the argument of \shapepar.
The macros work for both LaTeX and plain TeX. For LaTeX,
specify \usepackage{shapepar}; for Plain, \input shapepar.sty.
\shapepar works in terms of user-defined shapes, though the
package does provide some predefined shapes: so you can form
any paragraph into the form of a heart by putting
\heartpar{sometext...} inside your document. The tedium of
creating these polygon definitions may be alleviated by using
the shapepatch extension to transfig which will convert xfig
output to \shapepar polygon form.

%package -n texlive-shapepar-doc
Summary:        Documentation for shapepar
Version:        svn30708.2.2

Provides:       tex-shapepar-doc
AutoReqProv:    No

%description -n texlive-shapepar-doc
Documentation for shapepar

%package -n texlive-shdoc
Provides:       tex-shdoc = %{tl_version}
License:        LPPL 1.3
Summary:        Float environment to document the shell commands of a terminal session
Version:        svn41991
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xcolor.sty), tex(float.sty), tex(caption.sty), tex(mdframed.sty)
Requires:       tex(kvoptions.sty)
Provides:       tex(shdoc.sty) = %{tl_version}

%description -n texlive-shdoc
The package provides a simple, though fancy float environment
to document terminal sessions -- like command executions or
shell operations. The look and feel of the package output
imitates the look of a shell prompt.

%package -n texlive-shdoc-doc
Summary:        Documentation for shdoc
Version:        svn41991
Provides:       tex-shdoc-doc
AutoReqProv:    No

%description -n texlive-shdoc-doc
Documentation for shdoc

%package -n texlive-shipunov
Provides:       tex-shipunov = %{tl_version}
License:        LPPL
Summary:        A collection of LaTeX packages and classes
Version:        svn29349.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty), tex(xtab.sty), tex(calc.sty), tex(xspace.sty)
Requires:       tex(ifthen.sty), tex(syntonly.sty), tex(footnpag.sty)
Provides:       tex(altverse.sty) = %{tl_version}, tex(autolist.sty) = %{tl_version}
Provides:       tex(biokey.sty) = %{tl_version}, tex(biolist.sty) = %{tl_version}
Provides:       tex(boldline.sty) = %{tl_version}, tex(cassete.cls) = %{tl_version}
Provides:       tex(classif2.sty) = %{tl_version}, tex(drcaps.sty) = %{tl_version}
Provides:       tex(etiketka.cls) = %{tl_version}, tex(flower.sty) = %{tl_version}
Provides:       tex(isyntax.sty) = %{tl_version}, tex(numerus.sty) = %{tl_version}
Provides:       tex(punct.sty) = %{tl_version}, tex(sltables.sty) = %{tl_version}
Provides:       tex(starfn.sty) = %{tl_version}

%description -n texlive-shipunov
The bundle collects packages and classes, along with one
bibliography style and examples and scripts for converting TeX
files. Many of the files in the collection are designed to
support field biologists and/or Russian writers, while others
have wider application. The collection includes (among others):
altverse, a simple verse typesetting package; autolist, which
provides various list formatting facilities; biokey, which
provides a mechanism for typesetting biological identification
lists; biolist, which typesets species lists; boldline, which
typesets heavier separating lines in tables; cassete, which
lays out audio cassette inserts; classif2, which typesets
classification lists; drcaps, which provides dropped capital
macros; etiketka, a class for typesetting business-card-sized
information (including business cards); flower, for typesetting
lists of flower formulae; isyntax; numerus; punct; sltables,
which develops on the stables package, for use in a LaTeX
context; and starfn.

%package -n texlive-shipunov-doc
Summary:        Documentation for shipunov
Version:        svn29349.1.1

Provides:       tex-shipunov-doc
AutoReqProv:    No

%description -n texlive-shipunov-doc
Documentation for shipunov

%package -n texlive-shorttoc
Provides:       tex-shorttoc = %{tl_version}
License:        LPPL
Summary:        Table of contents with different depths
Version:        svn15878.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(shorttoc.sty) = %{tl_version}

%description -n texlive-shorttoc
A package to create another table of contents with a different
depth, useful in large documents where a detailed table of
contents should be accompanied by a shorter one, giving only a
general overview of the main topics in the document.

%package -n texlive-shorttoc-doc
Summary:        Documentation for shorttoc
Version:        svn15878.1.3

Provides:       tex-shorttoc-doc
AutoReqProv:    No

%description -n texlive-shorttoc-doc
Documentation for shorttoc

%package -n texlive-show2e
Provides:       tex-show2e = %{tl_version}
License:        LPPL
Summary:        Variants of \show for LaTeX2e
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(show2e.sty) = %{tl_version}

%description -n texlive-show2e
This small package aims at making debugging (especially in an
interactive way) easier, by providing \show variants suited to
LaTeX2e commands (whether with optional arguments or robust)
and environments. The variant commands also display the
internal macros used by such commands, if any. The \showcs
variant helps with macros with exotic names.

%package -n texlive-show2e-doc
Summary:        Documentation for show2e
Version:        svn15878.1.0

Provides:       tex-show2e-doc
AutoReqProv:    No

%description -n texlive-show2e-doc
Documentation for show2e

%package -n texlive-showcharinbox
Provides:       tex-showcharinbox = %{tl_version}
License:        LPPL 1.3
Summary:        Show characters inside a box
Version:        svn29803.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(showcharinbox.sty) = %{tl_version}

%description -n texlive-showcharinbox
The package typesets a character inside a box, showing where
reference point is, and displaying width, height, and depth
information of the character. The output is like that on page
63 of "The TeXBook" or page 101 of "The METAFONTbook". The
package itself is motivated by Knuth's macros in the file
manmac.tex. Users should note that using a small size for the
character inside the box does not make any sense: use a large
size.

%package -n texlive-showcharinbox-doc
Summary:        Documentation for showcharinbox
Version:        svn29803.0.1

Provides:       tex-showcharinbox-doc
AutoReqProv:    No

%description -n texlive-showcharinbox-doc
Documentation for showcharinbox

%package -n texlive-showdim
Provides:       tex-showdim = %{tl_version}
License:        LPPL
Summary:        Variants on printing dimensions
Version:        svn28918.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(showdim.sty) = %{tl_version}

%description -n texlive-showdim
A package for LaTeX providing a number of commands for printing
the value of a TeX dimension. For example,
\tenthpt{\baselineskip} yields the current value of
\baselineskip rounded to the nearest tenth of a point.

%package -n texlive-showdim-doc
Summary:        Documentation for showdim
Version:        svn28918.1.2

Provides:       tex-showdim-doc
AutoReqProv:    No

%description -n texlive-showdim-doc
Documentation for showdim

%package -n texlive-showexpl
Provides:       tex-showexpl = %{tl_version}
License:        LPPL
Summary:        Typesetting LaTeX source code
Version:        svn42677
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(attachfile.sty), tex(listings.sty), tex(calc.sty), tex(ifthen.sty)
Requires:       tex(graphicx.sty), tex(varwidth.sty)
Provides:       tex(showexpl.sty) = %{tl_version}

%description -n texlive-showexpl
This package provides a way to typeset LaTeX source code and
the related result in the same document.

%package -n texlive-showexpl-doc
Summary:        Documentation for showexpl
Version:        svn42677
Provides:       tex-showexpl-doc
AutoReqProv:    No

%description -n texlive-showexpl-doc
Documentation for showexpl

%package -n texlive-showlabels
Provides:       tex-showlabels = %{tl_version}
License:        GPL+
Summary:        Show label commands in the margin
Version:        svn41322

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(showlabels.sty) = %{tl_version}

%description -n texlive-showlabels
This package helps you keep track of all the labels you define,
by putting the name of new labels into the margin whenever the
\label command is used. The package allows you to do the same
thing for other commands. The only one for which this is
obviously useful is the \cite command, but it's easy to do it
for others, such as the \ref or \begin commands.

%package -n texlive-showlabels-doc
Summary:        Documentation for showlabels
Version:        svn41322

Provides:       tex-showlabels-doc
AutoReqProv:    No

%description -n texlive-showlabels-doc
Documentation for showlabels

%package -n texlive-sidecap
Provides:       tex-sidecap = %{tl_version}
License:        LPPL
Summary:        Typeset captions sideways
Version:        svn15878.1.6f

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(ragged2e.sty)
Provides:       tex(sidecap.sty) = %{tl_version}

%description -n texlive-sidecap
Defines environments called SCfigure and SCtable (analogous to
figure and table) to typeset captions sideways. Options include
outercaption, innercaption, leftcaption and rightcaption.

%package -n texlive-sidecap-doc
Summary:        Documentation for sidecap
Version:        svn15878.1.6f

Provides:       tex-sidecap-doc
AutoReqProv:    No

%description -n texlive-sidecap-doc
Documentation for sidecap

%package -n texlive-sidenotes
Provides:       tex-sidenotes = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset notes containing rich content, in the margin
Version:        svn40658

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(mhchem.sty), tex(morefloats.sty), tex(marginfix.sty)
Requires:       tex(microtype.sty), tex(geometry.sty), tex(ifluatex.sty), tex(fontspec.sty)
Requires:       tex(unicode-math.sty), tex(mathpazo.sty)
Requires:       tex(helvet.sty), tex(beramono.sty), tex(fontenc.sty), tex(titlesec.sty)
Requires:       tex(titletoc.sty), tex(fancyhdr.sty), tex(ragged2e.sty), tex(enumitem.sty)
Requires:       tex(textcase.sty), tex(color.sty), tex(l3keys2e.sty), tex(marginnote.sty)
Requires:       tex(caption.sty), tex(xparse.sty), tex(changepage.sty)
Provides:       tex(caesar_book.cls) = %{tl_version}, tex(sidenotes.sty) = %{tl_version}

%description -n texlive-sidenotes
The package allows typesetting of texts with notes, figures,
citations, captions and tables in the margin. This is common
(for example) in science text books.

%package -n texlive-sidenotes-doc
Summary:        Documentation for sidenotes
Version:        svn40658

Provides:       tex-sidenotes-doc
AutoReqProv:    No

%description -n texlive-sidenotes-doc
Documentation for sidenotes

%package -n texlive-silence
Provides:       tex-silence = %{tl_version}
License:        LPPL
Summary:        Selective filtering of error messages and warnings
Version:        svn27028.1.5b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(silence.sty) = %{tl_version}

%description -n texlive-silence
The package allows the user to filter out unwanted warnings and
error messages issued by LaTeX, packages and classes, so they
won't pop out when there's nothing one can do about them.
Filtering goes from the very broad ("avoid all messages by such
and such") to the fine-grained ("avoid messages that begin
with..."). Messages may be saved to an external file for later
reference.

%package -n texlive-silence-doc
Summary:        Documentation for silence
Version:        svn27028.1.5b

Provides:       tex-silence-doc
AutoReqProv:    No

%description -n texlive-silence-doc
Documentation for silence

%package -n texlive-simplecd
Provides:       tex-simplecd = %{tl_version}
License:        LPPL 1.2
Summary:        Simple CD, DVD covers for printing
Version:        svn29260.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fix-cm.sty), tex(calc.sty), tex(ifthen.sty), tex(graphicx.sty)
Provides:       tex(simplecd.sty) = %{tl_version}

%description -n texlive-simplecd
The package provides printable cut-outs for various CD, DVD and
other disc holders. The name of the package comes from its
implementation and ease of use; it was designed just for text
content, but since the text is placed in a \parbox in a tabular
environment cell, a rather wide range of things may be placed.

%package -n texlive-simplecd-doc
Summary:        Documentation for simplecd
Version:        svn29260.1.4

Provides:       tex-simplecd-doc
AutoReqProv:    No

%description -n texlive-simplecd-doc
Documentation for simplecd

%package -n texlive-simplecv
Provides:       tex-simplecv = %{tl_version}
License:        LPPL
Summary:        A simple class for writing curricula vitae
Version:        svn35537.1.6a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(simplecv.cls) = %{tl_version}
Obsoletes:      tex-simplecv < %{tl_version}

%description -n texlive-simplecv
A derivative of the cv class available to lyx users (renamed to
avoid the existing cv package).

%package -n texlive-simplecv-doc
Summary:        Documentation for simplecv
Version:        svn35537.1.6a

Provides:       tex-simplecv-doc
AutoReqProv:    No

%description -n texlive-simplecv-doc
Documentation for simplecv

%package -n texlive-simplewick
Provides:       tex-simplewick = %{tl_version}
License:        GPL+
Summary:        Simple Wick contractions
Version:        svn15878.1.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(simplewick.sty) = %{tl_version}

%description -n texlive-simplewick
The package provides a simple means of drawing Wick
contractions above and below expressions.

%package -n texlive-simplewick-doc
Summary:        Documentation for simplewick
Version:        svn15878.1.2a

Provides:       tex-simplewick-doc
AutoReqProv:    No

%description -n texlive-simplewick-doc
Documentation for simplewick

%package -n texlive-simplified-latex-doc
Summary:        Documentation for simplified-latex
Version:        svn20620.0

Provides:       tex-simplified-latex-doc
AutoReqProv:    No

%description -n texlive-simplified-latex-doc
Documentation for simplified-latex

%package -n texlive-simurgh
Provides:       tex-simurgh = %{tl_version}
License:        GPLv2+
Summary:        Typeset Parsi in LuaLaTeX
Version:        svn31719.0.01b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(simurgh-extbook.sty)
Requires:       tex(simurgh-extreport.sty), tex(simurgh-memoir.sty)
Requires:       tex(simurgh-rapport3.sty), tex(simurgh-report.sty)
Requires:       tex(simurgh-scrbook.sty), tex(simurgh-scrreprt.sty)
Requires:       tex(simurgh-tartibi.sty), tex(xcolor.sty)
Requires:       tex(minted.sty), tex(graphicx.sty), tex(fontspec.sty), tex(hyperref.sty)
Requires:       tex(geometry.sty), tex(makeidx.sty), tex(microtype.sty), tex(zref-abspage.sty)
Requires:       tex(auxhook.sty), tex(ltxcmds.sty), tex(pdftexcmds.sty), tex(xkeyval.sty)
Provides:       tex(simurgh-abjad.sty) = %{tl_version}, tex(simurgh-adadi.sty) = %{tl_version}
Provides:       tex(simurgh-algorithm.sty) = %{tl_version}
Provides:       tex(simurgh-algorithmic.sty) = %{tl_version}
Provides:       tex(simurgh-amsart.sty) = %{tl_version}, tex(simurgh-amsbook.sty) = %{tl_version}
Provides:       tex(simurgh-amsmath.sty) = %{tl_version}
Provides:       tex(simurgh-amstext.sty) = %{tl_version}
Provides:       tex(simurgh-amsthm.sty) = %{tl_version}, tex(simurgh-array.sty) = %{tl_version}
Provides:       tex(simurgh-article.sty) = %{tl_version}
Provides:       tex(simurgh-artikel1.sty) = %{tl_version}
Provides:       tex(simurgh-artikel2.sty) = %{tl_version}
Provides:       tex(simurgh-artikel3.sty) = %{tl_version}
Provides:       tex(simurgh-arydshln.sty) = %{tl_version}
Provides:       tex(simurgh-backref.sty) = %{tl_version}
Provides:       tex(simurgh-bidi.sty) = %{tl_version}, tex(simurgh-boek.sty) = %{tl_version}
Provides:       tex(simurgh-boek3.sty) = %{tl_version}, tex(simurgh-book.sty) = %{tl_version}
Provides:       tex(simurgh-bookest.sty) = %{tl_version}
Provides:       tex(simurgh-caption3.sty) = %{tl_version}
Provides:       tex(simurgh-chkeng.sty) = %{tl_version}, tex(simurgh-clss.sty) = %{tl_version}
Provides:       tex(simurgh-counters.sty) = %{tl_version}
Provides:       tex(simurgh-cptns.sty) = %{tl_version}, tex(simurgh-doc.cls) = %{tl_version}
Provides:       tex(simurgh-empheq.sty) = %{tl_version}, tex(simurgh-extarticle.sty) = %{tl_version}
Provides:       tex(simurgh-extbook.sty) = %{tl_version}
Provides:       tex(simurgh-extletter.sty) = %{tl_version}
Provides:       tex(simurgh-extreport.sty) = %{tl_version}
Provides:       tex(simurgh-fleqn.sty) = %{tl_version}, tex(simurgh-fonts.sty) = %{tl_version}
Provides:       tex(simurgh-footnotes.sty) = %{tl_version}
Provides:       tex(simurgh-ftnxtra.sty) = %{tl_version}
Provides:       tex(simurgh-glossaries.sty) = %{tl_version}
Provides:       tex(simurgh-harfi.sty) = %{tl_version}, tex(simurgh-jalalical.sty) = %{tl_version}
Provides:       tex(simurgh-leqno.sty) = %{tl_version}, tex(simurgh-letter.sty) = %{tl_version}
Provides:       tex(simurgh-lettrine.sty) = %{tl_version}
Provides:       tex(simurgh-loader.sty) = %{tl_version}, tex(simurgh-ltx.sty) = %{tl_version}
Provides:       tex(simurgh-mathdigitspec.sty) = %{tl_version}
Provides:       tex(simurgh-memoir.sty) = %{tl_version}, tex(simurgh-minitoc.sty) = %{tl_version}
Provides:       tex(simurgh-natbib.sty) = %{tl_version}, tex(simurgh-pkgs.sty) = %{tl_version}
Provides:       tex(simurgh-poem.sty) = %{tl_version}, tex(simurgh-rapport1.sty) = %{tl_version}
Provides:       tex(simurgh-rappport1.sty) = %{tl_version}
Provides:       tex(simurgh-rapport3.sty) = %{tl_version}
Provides:       tex(simurgh-refrep.sty) = %{tl_version}, tex(simurgh-report.sty) = %{tl_version}
Provides:       tex(simurgh-scrartcl.sty) = %{tl_version}
Provides:       tex(simurgh-scrbook.sty) = %{tl_version}
Provides:       tex(simurgh-scrlettr.sty) = %{tl_version}
Provides:       tex(simurgh-scrreprt.sty) = %{tl_version}
Provides:       tex(simurgh-shellescape.sty) = %{tl_version}
Provides:       tex(simurgh-tags.sty) = %{tl_version}, tex(simurgh-tartibi.sty) = %{tl_version}
Provides:       tex(simurgh-tools.sty) = %{tl_version}, tex(simurgh-unibidi.sty) = %{tl_version}
Provides:       tex(simurgh.sty) = %{tl_version}

%description -n texlive-simurgh
The package provides an automatic and unified interface for
Parsi typesetting in LaTeX, using the LuaTeX engine. The
project to produce this system is dedicated to Ferdowsi The
Great.

%package -n texlive-simurgh-doc
Summary:        Documentation for simurgh
Version:        svn31719.0.01b

Provides:       tex-simurgh-doc
AutoReqProv:    No

%description -n texlive-simurgh-doc
Documentation for simurgh

%package -n texlive-sitem
Provides:       tex-sitem = %{tl_version}
License:        LPPL 1.3
Summary:        Save the optional argument of \item
Version:        svn22136.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sitem.sty) = %{tl_version}

%description -n texlive-sitem
The package modifies \item commands to save the optional
argument in a box.

%package -n texlive-sitem-doc
Summary:        Documentation for sitem
Version:        svn22136.1.0

Provides:       tex-sitem-doc
AutoReqProv:    No

%description -n texlive-sitem-doc
Documentation for sitem

%package -n texlive-skb
Provides:       tex-skb = %{tl_version}
License:        LPPL 1.3
Summary:        Tools for a repository of long-living documents
Version:        svn22781.0.52

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(listings.sty), tex(dirtree.sty), tex(ifpdf.sty)
Requires:       tex(datetime.sty), tex(versions.sty), tex(booktabs.sty), tex(optional.sty)
Requires:       tex(biblatex.sty), tex(acronym.sty), tex(etoolbox.sty), tex(comment.sty)
Requires:       tex(graphicx.sty), tex(longtable.sty), tex(colortbl.sty), tex(textcomp.sty)
Requires:       tex(gensymb.sty), tex(wasysym.sty), tex(units.sty), tex(xmpmulti.sty)
Requires:       tex(float.sty), tex(xcolor.sty), tex(hyperref.sty), tex(beamerarticle.sty)
Requires:       tex(pgf.sty), tex(enumitem.sty)
Provides:       tex(skb.cfg) = %{tl_version}, tex(skb.sty) = %{tl_version}
Provides:       tex(skbarticle.cls) = %{tl_version}, tex(skbbeamer.cls) = %{tl_version}
Provides:       tex(skbbook.cls) = %{tl_version}, tex(skblncsbeamer.cls) = %{tl_version}
Provides:       tex(skblncsppt.cls) = %{tl_version}, tex(skbmoderncv.cls) = %{tl_version}

%description -n texlive-skb
The package provides macros that help to build a document
repository for long living documents. It focuses on structure
and re-use of text, code, figures etc. The basic concept is
first to separate structure from content (i.e., text about a
topic from the structure it is presented by) and then
separating the content from the actual published document, thus
enabling easy re-use of text blocks in different publications
(i.e., text about a protocol in a short article about this
protocol as well as in a book about many protocols); all
without constantly copying or changing text. As a side effect,
using the document classes provided, it hides a lot of LaTeX
from someone who just wants to write articles and books.

%package -n texlive-skb-doc
Summary:        Documentation for skb
Version:        svn22781.0.52

Provides:       tex-skb-doc
AutoReqProv:    No

%description -n texlive-skb-doc
Documentation for skb

%package -n texlive-skdoc
Provides:       tex-skdoc = %{tl_version}
License:        LPPL 1.3
Summary:        Documentation and extraction for packages and document classes
Version:        svn47526
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(etoolbox.sty), tex(xstring.sty), tex(xparse.sty)
Requires:       tex(atbegshi.sty), tex(kvoptions.sty), tex(pdftexcmds.sty), tex(everyhook.sty)
Requires:       tex(verbatim.sty), tex(needspace.sty), tex(marginnote.sty), tex(calc.sty)
Requires:       tex(hyperref.sty), tex(multicol.sty), tex(hologo.sty), tex(glossaries.sty)
Requires:       tex(ydoc-code.sty), tex(ydoc-desc.sty), tex(scrpage2.sty), tex(babel.sty)
Requires:       tex(csquotes.sty), tex(caption.sty), tex(PTSerif.sty), tex(sourcecodepro.sty)
Requires:       tex(opensans.sty), tex(microtype.sty), tex(minted.sty)
Provides:       tex(skdoc.cls) = %{tl_version}

%description -n texlive-skdoc
The class provides the functionality and implementation of
packages and document classes. It is loosely based on the ydoc
and ltxdoc classes, but has a number of incompatible
differences. The class defines a MacroCode environment which
offers an alternative to the the usual docstrip method of
installing packages. It has the ability to generate both
documentation and code in a single run of a single file.

%package -n texlive-skdoc-doc
Summary:        Documentation for skdoc
Version:        svn47526
Provides:       tex-skdoc-doc
AutoReqProv:    No

%description -n texlive-skdoc-doc
Documentation for skdoc

%package -n texlive-skeycommand
Provides:       tex-skeycommand = %{tl_version}
License:        LPPL 1.3
Summary:        Create commands using parameters and keyval in parallel
Version:        svn24652.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(catoptions.sty)
Provides:       tex(skeycommand.sty) = %{tl_version}

%description -n texlive-skeycommand
The package provides tools for defining LaTeX commands and
environments using combinations of parameters and keys. All the
facilities of the ltxkeys and skeyval packages are available to
the user of skeycommand.

%package -n texlive-skeycommand-doc
Summary:        Documentation for skeycommand
Version:        svn24652.0.4

Provides:       tex-skeycommand-doc
AutoReqProv:    No

%description -n texlive-skeycommand-doc
Documentation for skeycommand

%package -n texlive-skeyval
Provides:       tex-skeyval = %{tl_version}
License:        LPPL 1.3
Summary:        Key-value parsing combining features of xkeyval and pgfkeys
Version:        svn30560.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(atveryend.sty), tex(xcolor.sty), tex(pifont.sty)
Requires:       tex(tikz.sty), tex(graphicx.sty), tex(longtable.sty)
Provides:       tex(skeyval-bc.sty) = %{tl_version}, tex(skeyval.sty) = %{tl_version}
Provides:       tex(skeyval-core.tex) = %{tl_version}, tex(skeyval-for.tex) = %{tl_version}
Provides:       tex(skeyval-ltxcmds.tex) = %{tl_version}
Provides:       tex(skeyval-ltxpatch.sty) = %{tl_version}
Provides:       tex(skeyval-pstkey.sty) = %{tl_version}, tex(skeyval-pstkey.tex) = %{tl_version}
Provides:       tex(skeyval-testclass.cls) = %{tl_version}
Provides:       tex(skeyval-testpkg.sty) = %{tl_version}
Provides:       tex(skeyval-view.sty) = %{tl_version}, tex(skeyval.sty) = %{tl_version}

%description -n texlive-skeyval
The package integrates the features of xkeyval and of pgfkeys
by introducing a new type of handlers. Style keys, links,
changing key callbacks and values on the fly, and other
features of pgfkeys are introduced in a new context.

%package -n texlive-skeyval-doc
Summary:        Documentation for skeyval
Version:        svn30560.1.3

Provides:       tex-skeyval-doc
AutoReqProv:    No

%description -n texlive-skeyval-doc
Documentation for skeyval

%package -n texlive-skrapport
Provides:       tex-skrapport = %{tl_version}
License:        LPPL 1.3
Summary:        'Simple' class for reports, etc
Version:        svn45304
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(typearea.sty), tex(etoolbox.sty), tex(grid.sty)
Requires:       tex(babel.sty), tex(fontspec.sty), tex(kpfonts.sty), tex(lmodern.sty)
Requires:       tex(arev.sty), tex(pxfonts.sty), tex(tgpagella.sty), tex(mathpazo.sty)
Requires:       tex(MnSymbol.sty), tex(PTSerif.sty), tex(opensans.sty), tex(sourcecodepro.sty)
Requires:       tex(amsmath.sty), tex(amssymb.sty), tex(textcomp.sty), tex(skmath.sty)
Requires:       tex(xcolor.sty), tex(unicode-math.sty), tex(polyglossia.sty), tex(fontenc.sty)
Requires:       tex(isomath.sty), tex(xkeyval.sty), tex(calc.sty), tex(isodate.sty)
Requires:       tex(multicol.sty), tex(microtype.sty)
Provides:       tex(skrapport-colortheme-cruelwater.sty) = %{tl_version}
Provides:       tex(skrapport-colortheme-default.sty) = %{tl_version}
Provides:       tex(skrapport-colortheme-skdoc.sty) = %{tl_version}
Provides:       tex(skrapport-colortheme-unscathed.sty) = %{tl_version}
Provides:       tex(skrapport-colortheme-violet.sty) = %{tl_version}
Provides:       tex(skrapport-size-common.sty) = %{tl_version}
Provides:       tex(skrapport-size10pt.clo) = %{tl_version}
Provides:       tex(skrapport-size11pt.clo) = %{tl_version}
Provides:       tex(skrapport-size12pt.clo) = %{tl_version}
Provides:       tex(skrapport.cls) = %{tl_version}

%description -n texlive-skrapport
The class is intended for simple documents (e.g., reports
handed in as coursework and the like). The class is small and
straightforward; its design was inspired by that of the PracTeX
journal style.

%package -n texlive-skrapport-doc
Summary:        Documentation for skrapport
Version:        svn45304
Provides:       tex-skrapport-doc
AutoReqProv:    No

%description -n texlive-skrapport-doc
Documentation for skrapport

%package -n texlive-slantsc
Provides:       tex-slantsc = %{tl_version}
License:        LPPL
Summary:        Access different-shaped small-caps fonts
Version:        svn25007.2.11

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(slantsc.sty) = %{tl_version}

%description -n texlive-slantsc
This package enables the use of small capitals in different
font shapes, e.g., slanted or bold slanted for all fonts that
provide appropriate font shapes. (Note that a separate .fd file
is needed to define font shapes such as 'scsl' or 'scit'.)

%package -n texlive-slantsc-doc
Summary:        Documentation for slantsc
Version:        svn25007.2.11

Provides:       tex-slantsc-doc
AutoReqProv:    No

%description -n texlive-slantsc-doc
Documentation for slantsc

%package -n texlive-smalltableof
Provides:       tex-smalltableof = %{tl_version}
License:        LPPL
Summary:        Create listoffigures etc. in a single chapter
Version:        svn20333.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(smalltableof.sty) = %{tl_version}

%description -n texlive-smalltableof
The package allows you to create a list of figures and list of
tables in a chapter named 'List' that contains separate
sections for each list of figures, tables, etc.

%package -n texlive-smalltableof-doc
Summary:        Documentation for smalltableof
Version:        svn20333.0

Provides:       tex-smalltableof-doc
AutoReqProv:    No

%description -n texlive-smalltableof-doc
Documentation for smalltableof

%package -n texlive-smartdiagram
Provides:       tex-smartdiagram = %{tl_version}
License:        LPPL 1.3
Summary:        Generate diagrams from lists
Version:        svn42781
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty), tex(etoolbox.sty), tex(xparse.sty), tex(xstring.sty)
Provides:       tex(smartdiagram.sty) = %{tl_version}, tex(smartdiagramlibraryadditions.code.tex) = %{tl_version}
Provides:       tex(smartdiagramlibrarycore.commands.code.tex) = %{tl_version}
Provides:       tex(smartdiagramlibrarycore.definitions.code.tex) = %{tl_version}
Provides:       tex(smartdiagramlibrarycore.styles.code.tex) = %{tl_version}

%description -n texlive-smartdiagram
The package will create 'smart' diagrams from lists of items,
for simple documents and for presentations.

%package -n texlive-smartdiagram-doc
Summary:        Documentation for smartdiagram
Version:        svn42781
Provides:       tex-smartdiagram-doc
AutoReqProv:    No

%description -n texlive-smartdiagram-doc
Documentation for smartdiagram

%package -n texlive-spath3
Provides:       tex-spath3 = %{tl_version}
License:        LPPL 1.3
Summary:        Manipulate "soft paths" in PGF
Version:        svn39794

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(pgf.sty), tex(xparse.sty)
Provides:       tex(spath3.sty) = %{tl_version}, tex(tikzlibrarycalligraphy.code.tex) = %{tl_version}
Provides:       tex(tikzlibraryknots.code.tex) = %{tl_version}

%description -n texlive-spath3
The spath3 library provides methods for manipulating the "soft
paths" of TikZ/PGF. Packaged with it are two TikZ libraries
that make use of the methods provided. These are libraries for
drawing calligraphic paths and for drawing knot diagrams.

%package -n texlive-spath3-doc
Summary:        Documentation for spath3
Version:        svn39794

Provides:       tex-spath3-doc
AutoReqProv:    No

%description -n texlive-spath3-doc
Documentation for spath3

%package -n texlive-swimgraf
Provides:       tex-swimgraf = %{tl_version}
License:        LPPL
Summary:        Graphical/textual representations of swimming performances
Version:        svn25446.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(mathpazo.sty), tex(pstricks.sty), tex(pstcol.sty), tex(pst-plot.sty)
Requires:       tex(keyval.sty)
Provides:       tex(swimgraf.cfg) = %{tl_version}, tex(swimgraf.sty) = %{tl_version}

%description -n texlive-swimgraf
The package provides two macros that produce representations of
a swimmer's performances. The user records data in a text file
and specifies as arguments of the macros the date range of
interest. The macros extract the relevant information from the
file and process it: \swimgraph produces a graph of the times
in a single swimming event (specified as an argument), plotting
long course and short course times in separate lines. Records
and qualifying times, stored in text files, may optionally be
included on the graph. \swimtext produces a written record of
the times in all events. Files of current world and Canadian
records are included. The package requires the PSTricks and
keyval packages. For attractive output it also requires a
colour output device.

%package -n texlive-swimgraf-doc
Summary:        Documentation for swimgraf
Version:        svn25446.0

Provides:       tex-swimgraf-doc
AutoReqProv:    No

%description -n texlive-swimgraf-doc
Documentation for swimgraf

%package -n texlive-smartref
Provides:       tex-smartref = %{tl_version}
License:        LPPL
Summary:        Extend LaTeX's \ref capability
Version:        svn20311.1.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(byname.sty) = %{tl_version}, tex(smartref.sty) = %{tl_version}

%description -n texlive-smartref
The package extends the LaTeX labelling system: whenever a
label is set, the values of counters (selected by the user) are
recorded, along with the label. The value of these counters can
be recalled with a command similar to \pageref. The package
also adds commands \s[name]ref (for each counter [name] that
the user has selected); these commands display something only
if the value of the [name] counter is changed from when the
label was set. Many commands are provided to serve as a macro
programming environment for using the extended labels.

%package -n texlive-smartref-doc
Summary:        Documentation for smartref
Version:        svn20311.1.9

Provides:       tex-smartref-doc
AutoReqProv:    No

%description -n texlive-smartref-doc
Documentation for smartref

%package -n texlive-snapshot
Provides:       tex-snapshot = %{tl_version}
License:        LPPL
Summary:        List the external dependencies of a LaTeX document
Version:        svn15878.1.14

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(snapshot.sty) = %{tl_version}

%description -n texlive-snapshot
The snapshot package helps the owner of a LaTeX document obtain
a list of the external dependencies of the document, in a form
that can be embedded at the top of the document. It provides a
snapshot of the current processing context of the document,
insofar as it can be determined from inside LaTeX. If a
document contains such a dependency list, then it becomes
possible to arrange that the document be processed always with
the same versions of everything, in order to ensure the same
output. This could be useful for someone wanting to keep a
LaTeX document on hand and consistently reproduce an identical
DVI file from it, on the fly; or for someone wanting to shield
a document during the final stages of its production cycle from
unexpected side effects of routine upgrades to the TeX system.

%package -n texlive-snapshot-doc
Summary:        Documentation for snapshot
Version:        svn15878.1.14

Provides:       tex-snapshot-doc
AutoReqProv:    No

%description -n texlive-snapshot-doc
Documentation for snapshot

%package -n texlive-snotez
Provides:       tex-snotez = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset notes, in the margin
Version:        svn30355.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(pgfopts.sty), tex(marginnote.sty), tex(perpage.sty)
Provides:       tex(snotez.sty) = %{tl_version}

%description -n texlive-snotez
The package provides a macro \sidenote, that places a note in
the margin of the document, with its baseline aligned with the
baseline in the body of the document. These sidenotes are
numbered (both in the text, and on the notes themselves). The
package loads the package etoolbox, pgfopts, marginnote and
perpage.

%package -n texlive-snotez-doc
Summary:        Documentation for snotez
Version:        svn30355.0.3

Provides:       tex-snotez-doc
AutoReqProv:    No

%description -n texlive-snotez-doc
Documentation for snotez

%package -n texlive-songbook
Provides:       tex-songbook = %{tl_version}
License:        LGPLv2+
Summary:        Package for typesetting song lyrics and chord books
Version:        svn18136.4.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(ifthen.sty), tex(xstring.sty), tex(multicol.sty)
Provides:       tex(conditionals.sty) = %{tl_version}, tex(songbook.sty) = %{tl_version}

%description -n texlive-songbook
The package provides an all purpose songbook style. Three types
of output may be created from a single input file: "words and
chords" books for the musicians to play from, "words only"
songbooks for the congregation to sing from, and overhead
transparency masters for congregational use. The package will
also print a table of contents, an index sorted by title and
first line, and an index sorted by key, or by artist/composer.
The package attempts to handle songs in multiple keys, as well
as songs in multiple languages.

%package -n texlive-songbook-doc
Summary:        Documentation for songbook
Version:        svn18136.4.5

Provides:       tex-songbook-doc
AutoReqProv:    No

%description -n texlive-songbook-doc
Documentation for songbook

%package -n texlive-songs
Provides:       tex-songs = %{tl_version}
License:        GPL+
Summary:        Produce song books for church or fellowship
Version:        svn44553
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etex.sty), tex(keyval.sty), tex(color.sty)
Provides:       tex(songs.sty) = %{tl_version}

%description -n texlive-songs
The package provides a means of producing beautiful song books
for church or fellowship. It offers: a very easy chord-entry
syntax; multiple modes (words-only; words+chords; slides;
handouts); measure bars; guitar tablatures; automatic
transposition; scripture quotations; multiple indexes (sorted
by title, author, important lyrics, or scripture references);
and projector-style output generation, for interactive use. A
set of example documents is provided.

%package -n texlive-songs-doc
Summary:        Documentation for songs
Version:        svn44553
Provides:       tex-songs-doc
AutoReqProv:    No

%description -n texlive-songs-doc
Documentation for songs

%package -n texlive-soul
Provides:       tex-soul = %{tl_version}
License:        LPPL
Summary:        Hyphenation for letterspacing, underlining, and more
Version:        svn15878.2.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(soul.sty) = %{tl_version}

%description -n texlive-soul
Provides hyphenatable spacing out (letterspacing), underlining,
striking out, etc., using the TeX hyphenation algorithm to find
the proper hyphens automatically. The package also provides a
mechanism that can be used to implement similar tasks, that
have to treat text syllable by syllable. This is shown in two
examples. The package itself does not support UTF-8 input in
ordinary (PDF)LaTeX; some UTF-8 support is offered by package
soulutf8

%package -n texlive-soul-doc
Summary:        Documentation for soul
Version:        svn15878.2.4

Provides:       tex-soul-doc
AutoReqProv:    No

%description -n texlive-soul-doc
Documentation for soul

%package -n texlive-spanish-mx
Provides:       tex-spanish-mx = %{tl_version}
License:        LPPL
Summary:        Typeset Spanish as in Mexico
Version:        svn15878.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(esmx.cfg) = %{tl_version}, tex(spanishmx.ldf) = %{tl_version}
Provides:       tex(spanishmx.sty) = %{tl_version}

%description -n texlive-spanish-mx
The bundle provides files to support typesetting of texts in
Spanish according to Mexican current practices, using babel.
The files merge earlier work on a mexican.ldf, or may be used
to define a configuration that will typeset all documents (that
request babel's spanish option) to use the Mexican language
facilities. (Note that this facility is only available with the
recent (version >=4.2b) releases of the Spanish option.)

%package -n texlive-spanish-mx-doc
Summary:        Documentation for spanish-mx
Version:        svn15878.1.1a

Provides:       tex-spanish-mx-doc
AutoReqProv:    No

%description -n texlive-spanish-mx-doc
Documentation for spanish-mx

%package -n texlive-sparklines
Provides:       tex-sparklines = %{tl_version}
License:        LPPL
Summary:        Drawing sparklines: intense, simple, wordlike graphics
Version:        svn42821
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(pgf.sty)
Provides:       tex(sparklines.sty) = %{tl_version}

%description -n texlive-sparklines
Sparklines are intense, simple, wordlike graphics (so named by
Edward Tufte). In lieu of a more detailed introduction,
Professor Tufte's site has an early release of a chapter on
sparklines. A PHP implementation may be found at SourceForge. A
sparkline can be added using the sparkline environment. Also,
you can add sparkling rectangles for the median and special
sparkling dots in red or blue. The package requires pdflatex;
sparklines cannot appear in a dvi file. The sparklines package
uses pgf, and does not work with pictex.

%package -n texlive-sparklines-doc
Summary:        Documentation for sparklines
Version:        svn42821
Provides:       tex-sparklines-doc
AutoReqProv:    No

%description -n texlive-sparklines-doc
Documentation for sparklines

%package -n texlive-sphack
Provides:       tex-sphack = %{tl_version}
License:        Bibtex
Summary:        Patch LaTeX kernel spacing macros
Version:        svn20842.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sphack.sty) = %{tl_version}

%description -n texlive-sphack
Change the kernel internal \@bsphack/\@esphack so that it is
also invisible in vertical mode.

%package -n texlive-sphack-doc
Summary:        Documentation for sphack
Version:        svn20842.0

Provides:       tex-sphack-doc
AutoReqProv:    No

%description -n texlive-sphack-doc
Documentation for sphack

%package -n texlive-spot
Provides:       tex-spot = %{tl_version}
License:        LPPL 1.3
Summary:        Spotlight highlighting for Beamer
Version:        svn22408.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(afterpage.sty)
Provides:       tex(spot.sty) = %{tl_version}

%description -n texlive-spot
The package allows dramatic highlighting of words and phrases
by painting shapes around them. It is chiefly intended for use
in Beamer presentations, but it can be used in other document
classes as well.

%package -n texlive-spot-doc
Summary:        Documentation for spot
Version:        svn22408.1.1

Provides:       tex-spot-doc
AutoReqProv:    No

%description -n texlive-spot-doc
Documentation for spot

%package -n texlive-spotcolor
Provides:       tex-spotcolor = %{tl_version}
License:        LPPL
Summary:        Spot colours for pdfLaTeX
Version:        svn15878.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(spotcolor.sty) = %{tl_version}, tex(spotcolorhks.tex) = %{tl_version}
Provides:       tex(spotcolorpantone.tex) = %{tl_version}

%description -n texlive-spotcolor
This package provides procedures for using spot colours in
LaTeX documents and the generated pdf files. Predefined
templates for PANTONE and HKS colour spaces are included but
new ones can easily be defined.

%package -n texlive-spotcolor-doc
Summary:        Documentation for spotcolor
Version:        svn15878.1.2

Provides:       tex-spotcolor-doc
AutoReqProv:    No

%description -n texlive-spotcolor-doc
Documentation for spotcolor

%package -n texlive-spreadtab
Provides:       tex-spreadtab = %{tl_version}
License:        LPPL 1.3
Summary:        Spreadsheet features for LaTeX tabular environments
Version:        svn46185
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fp.sty), tex(xstring.sty)
Provides:       tex(spreadtab.sty) = %{tl_version}

%description -n texlive-spreadtab
The package allows the user to construct tables in a manner
similar to a spreadsheet. The cells of a table have row and
column indices and these can be used in formulas to generate
values in other cells.

%package -n texlive-spreadtab-doc
Summary:        Documentation for spreadtab
Version:        svn46185
Provides:       tex-spreadtab-doc
AutoReqProv:    No

%description -n texlive-spreadtab-doc
Documentation for spreadtab

%package -n texlive-spverbatim
Provides:       tex-spverbatim = %{tl_version}
License:        LPPL
Summary:        Allow line breaks within \verb and verbatim output
Version:        svn15878.v1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(spverbatim.sty) = %{tl_version}

%description -n texlive-spverbatim
LaTeX's \verb macro treats its argument as an unbreakable unit
of text. This can lead to poor typesetting, especially when the
argument is long. The spverbatim package provides an \spverb
macro that is analogous to \verb and an spverbatim environment
that is analogous to verbatim with the difference being that
\spverb and spverbatim allow LaTeX to break lines at space
characters.

%package -n texlive-spverbatim-doc
Summary:        Documentation for spverbatim
Version:        svn15878.v1.0

Provides:       tex-spverbatim-doc
AutoReqProv:    No

%description -n texlive-spverbatim-doc
Documentation for spverbatim

%package -n texlive-srbook-mem
Provides:       tex-srbook-mem = %{tl_version}
License:        LPPL
Summary:        srbook-mem package
Version:        svn45818
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(srbook-mem.sty) = %{tl_version}

%description -n texlive-srbook-mem
srbook-mem package

%package -n texlive-srbook-mem-doc
Summary:        Documentation for srbook-mem
Version:        svn45818
Provides:       tex-srbook-mem-doc
AutoReqProv:    No

%description -n texlive-srbook-mem-doc
Documentation for srbook-mem

%package -n texlive-srcltx
Provides:       tex-srcltx = %{tl_version}
License:        Public Domain
Summary:        Jump between DVI and TeX files
Version:        svn15878.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(srcltx.sty) = %{tl_version}, tex(srctex.sty) = %{tl_version}

%description -n texlive-srcltx
Provides a \special insertion into generated .dvi files
allowing one to jump from the .dvi file to the .tex source and
back again (given a .dvi viewer that supports this, such as Yap
or xdvi version 22.38 or later). This was originally written by
Aleksander Simonic, the author of the WinEdt shell.

%package -n texlive-srcltx-doc
Summary:        Documentation for srcltx
Version:        svn15878.1.6

Provides:       tex-srcltx-doc
AutoReqProv:    No

%description -n texlive-srcltx-doc
Documentation for srcltx

%package -n texlive-sseq
Provides:       tex-sseq = %{tl_version}
License:        LPPL
Summary:        Typesetting spectral sequence charts
Version:        svn31585.2.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(pifont.sty), tex(pgf.sty)
Requires:       tex(xkeyval.sty)
Provides:       tex(sseq.sty) = %{tl_version}

%description -n texlive-sseq
The package provides commands to draw spectral sequence
diagrams, providing facilities for clipping and arranging
multiple symbols so that they do not overlap. The package is
built using pgf, and shares that systems large demands for TeX
system memory. Its geometric commands are based on a turtle
graphics model, and control structures such as loops and
conditionals are available.

%package -n texlive-sseq-doc
Summary:        Documentation for sseq
Version:        svn31585.2.01

Provides:       tex-sseq-doc
AutoReqProv:    No

%description -n texlive-sseq-doc
Documentation for sseq

%package -n texlive-sslides
Provides:       tex-sslides = %{tl_version}
License:        LPPL 1.3
Summary:        Slides with headers and footers
Version:        svn32293.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sslides.cls) = %{tl_version}

%description -n texlive-sslides
The class provides a variant of the LaTeX standard slides
class, in which the user may add headers and footers to the
slide.

%package -n texlive-sslides-doc
Summary:        Documentation for sslides
Version:        svn32293.0

Provides:       tex-sslides-doc
AutoReqProv:    No

%description -n texlive-sslides-doc
Documentation for sslides

%package -n texlive-stack
Provides:       tex-stack = %{tl_version}
License:        LPPL
Summary:        Tools to define and use stacks
Version:        svn15878.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(relinput.sty) = %{tl_version}, tex(stack.sty) = %{tl_version}

%description -n texlive-stack
The package provides a small set of commands to implement
stacks independently of TeX's own stack. As an example of how
the stacks might be used, the documentation offers a small
"relinput" package that implements the backbone of the import
package.

%package -n texlive-stackengine
Provides:       tex-stackengine = %{tl_version}
License:        LPPL 1.3
Summary:        Highly customised stacking of objects, insets, baseline changes, etc
Version:        svn43221
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(etoolbox.sty)
Provides:       tex(stackengine.sty) = %{tl_version}

%description -n texlive-stackengine
The package provides a versatile way to stack objects
vertically in a variety of customizable ways. A number of
useful macros are provided, all of which make use of the
stackengine core.

%package -n texlive-stackengine-doc
Summary:        Documentation for stackengine
Version:        svn43221
Provides:       tex-stackengine-doc
AutoReqProv:    No

%description -n texlive-stackengine-doc
Documentation for stackengine

%package -n texlive-standalone
Provides:       tex-standalone = %{tl_version}
License:        LPPL 1.3
Summary:        Compile TeX pictures stand-alone or as part of a document
Version:        svn47136
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifluatex.sty), tex(ifpdf.sty), tex(ifxetex.sty), tex(xkeyval.sty)
Requires:       tex(currfile-abspath.sty), tex(multido.sty)
Requires:       tex(varwidth.sty), tex(tikz.sty), tex(pstricks.sty), tex(currfile.sty)
Requires:       tex(trimclip.sty), tex(adjustbox.sty), tex(gincltex.sty), tex(filemod-expmin.sty)
Provides:       tex(standalone.cfg) = %{tl_version}, tex(standalone.cls) = %{tl_version}
Provides:       tex(standalone.sty) = %{tl_version}, tex(standalone.tex) = %{tl_version}

%description -n texlive-standalone
A class and package is provided which allows TeX pictures or
other TeX code to be compiled standalone or as part of a main
document. Special support for pictures with beamer overlays is
also provided. The package is used in the main document and
skips extra preambles in sub-files. The class may be used to
simplify the preamble in sub-files. By default the preview
package is used to display the typeset code without margins.
The behaviour in standalone mode may adjusted using a
configuration file standalone.cfg to redefine the standalone
environment.

%package -n texlive-standalone-doc
Summary:        Documentation for standalone
Version:        svn47136
Provides:       tex-standalone-doc
AutoReqProv:    No

%description -n texlive-standalone-doc
Documentation for standalone

%package -n texlive-statistik
Provides:       tex-statistik = %{tl_version}
License:        GPL+
Summary:        Store statistics of a document
Version:        svn20334.0.03

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(statistik.sty) = %{tl_version}

%description -n texlive-statistik
The package counts the numbers of pages per chapter, and stores
the results in a separate file; the format of the file is
selectable.

%package -n texlive-statistik-doc
Summary:        Documentation for statistik
Version:        svn20334.0.03

Provides:       tex-statistik-doc
AutoReqProv:    No

%description -n texlive-statistik-doc
Documentation for statistik

%package -n texlive-stdclsdv
Provides:       tex-stdclsdv = %{tl_version}
License:        LPPL
Summary:        Provide sectioning information for package writers
Version:        svn15878.1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(stdclsdv.sty) = %{tl_version}

%description -n texlive-stdclsdv
The stdclsdv package is designed for package writers who need
to know what sectioning divsions are provided by the document's
class. It also provides a version of \CheckCommand that sets a
flag rather than printing a warning.

%package -n texlive-stdclsdv-doc
Summary:        Documentation for stdclsdv
Version:        svn15878.1.1a

Provides:       tex-stdclsdv-doc
AutoReqProv:    No

%description -n texlive-stdclsdv-doc
Documentation for stdclsdv

%package -n texlive-stdpage
Provides:       tex-stdpage = %{tl_version}
License:        LPPL 1.2
Summary:        Standard pages with n lines of at most m characters each
Version:        svn15878.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(typearea.sty), tex(ragged2e.sty), tex(ifthen.sty), tex(keyval.sty)
Requires:       tex(lineno.sty), tex(hyphenat.sty), tex(titlesec.sty)
Provides:       tex(stdpage.sty) = %{tl_version}

%description -n texlive-stdpage
For translations, proofreading, journal contributions etc.
standard pages are used. Those standard pages consist of a
fixed number of lines and characters per line. This package
produces pages with n lines of at most m characters each. For
instance the German "Normseite": 60 lines of 30 characters
each.

%package -n texlive-stdpage-doc
Summary:        Documentation for stdpage
Version:        svn15878.0.6

Provides:       tex-stdpage-doc
AutoReqProv:    No

%description -n texlive-stdpage-doc
Documentation for stdpage

%package -n texlive-stex
Provides:       tex-stex = %{tl_version}
License:        LPPL
Summary:        An Infrastructure for Semantic Preloading of LaTeX Documents
Version:        svn40320

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(sref.sty), tex(graphicx.sty), tex(size10.clo), tex(rdfmeta.sty)
Requires:       tex(hwexam.sty), tex(a4wide.sty), tex(amssymb.sty), tex(amstext.sty)
Requires:       tex(amsmath.sty), tex(keyval.sty), tex(babel.sty), tex(marginnote.sty)
Requires:       tex(beamerarticle.sty), tex(tikz.sty), tex(url.sty), tex(comment.sty)
Requires:       tex(standalone.sty), tex(xspace.sty), tex(xcomment.sty), tex(longtable.sty)
Requires:       tex(ntheorem.sty), tex(pgf.sty)
Provides:       tex(cmath.sty) = %{tl_version}, tex(dcm.sty) = %{tl_version}
Provides:       tex(hwexam.cls) = %{tl_version}, tex(hwexam.sty) = %{tl_version}
Provides:       tex(metakeys.sty) = %{tl_version}, tex(beamerthemeJacobs.sty) = %{tl_version}
Provides:       tex(mikoaffiliation.sty) = %{tl_version}
Provides:       tex(mikoslides.cls) = %{tl_version}, tex(mikoslides.sty) = %{tl_version}
Provides:       tex(modules.sty) = %{tl_version}, tex(omdoc.cls) = %{tl_version}
Provides:       tex(omdoc.sty) = %{tl_version}, tex(omtext.sty) = %{tl_version}
Provides:       tex(presentation.sty) = %{tl_version}, tex(problem.sty) = %{tl_version}
Provides:       tex(rdfmeta.sty) = %{tl_version}, tex(reqdoc.sty) = %{tl_version}
Provides:       tex(smglom.sty) = %{tl_version}, tex(smultiling.sty) = %{tl_version}
Provides:       tex(sproof.sty) = %{tl_version}, tex(sref.sty) = %{tl_version}
Provides:       tex(statements.sty) = %{tl_version}, tex(stex.sty) = %{tl_version}
Provides:       tex(structview.sty) = %{tl_version}, tex(tikzinput.sty) = %{tl_version}
Provides:       tex(workaddress.sty) = %{tl_version}

%description -n texlive-stex
The sTeX package collection is a version of TeX/LaTeX that
allows to markup TeX/LaTeX documents semantically without
leaving the document format, essentially turning it into a
document format for mathematical knowledge management (MKM).

%package -n texlive-stex-doc
Summary:        Documentation for stex
Version:        svn40320

Provides:       tex-stex-doc
AutoReqProv:    No

%description -n texlive-stex-doc
Documentation for stex

%package -n texlive-storebox
Provides:       tex-storebox = %{tl_version}
License:        LPPL 1.3
Summary:        Storing information for reuse
Version:        svn24895.1.3a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty), tex(collectbox.sty)
Provides:       tex(storebox-pgf.sty) = %{tl_version}, tex(storebox.sty) = %{tl_version}

%description -n texlive-storebox
The package provides "store boxes" whose user interface matches
that of normal LaTeX "save boxes", except that the content of a
store box appears at most once in the output PDF file, however
often it is used. The present version of the package supports
pdfLaTeX and LuaLaTeX; when DVI is output, store boxes behave
the same as save boxes.

%package -n texlive-storebox-doc
Summary:        Documentation for storebox
Version:        svn24895.1.3a

Provides:       tex-storebox-doc
AutoReqProv:    No

%description -n texlive-storebox-doc
Documentation for storebox

%package -n texlive-storecmd
Provides:       tex-storecmd = %{tl_version}
License:        LPPL 1.3
Summary:        Store the name of a defined command in a container
Version:        svn24431.0.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(catoptions.sty), tex(ltxtools.sty)
Provides:       tex(storecmd.sty) = %{tl_version}

%description -n texlive-storecmd
The package provides macros for command definition that save
the name of the command being defined in a file or a macro
container. The list could be useful for spelling exceptions in
text editors that do not support TeX syntax.

%package -n texlive-storecmd-doc
Summary:        Documentation for storecmd
Version:        svn24431.0.0.2

Provides:       tex-storecmd-doc
AutoReqProv:    No

%description -n texlive-storecmd-doc
Documentation for storecmd

%package -n texlive-stringstrings
Provides:       tex-stringstrings = %{tl_version}
License:        LPPL 1.3
Summary:        String manipulation for cosmetic and programming application
Version:        svn36203.1.23

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(stringstrings.sty) = %{tl_version}

%description -n texlive-stringstrings
The package provides a large and sundry set of macros for the
manipulation of strings. The macros are developed not merely
for cosmetic application (such as changing the case of letters
and string substitution), but also for programming applications
such as character look-ahead, argument parsing, conditional
tests on various string conditions, etc. The macros were
designed all to be expandable (note that things such as
\uppercase and \lowercase are not expandable), so that the
macros may be strung together sequentially and nested (after a
fashion) to achieve rather complex manipulations.

%package -n texlive-stringstrings-doc
Summary:        Documentation for stringstrings
Version:        svn36203.1.23

Provides:       tex-stringstrings-doc
AutoReqProv:    No

%description -n texlive-stringstrings-doc
Documentation for stringstrings

%package -n texlive-sttools
Provides:       tex-sttools = %{tl_version}
License:        LPPL 1.3
Summary:        Various macros
Version:        svn43684
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(array.sty)
Provides:       tex(cuted.sty) = %{tl_version}, tex(floatpag.sty) = %{tl_version}
Provides:       tex(flushend.sty) = %{tl_version}, tex(marginal.sty) = %{tl_version}
Provides:       tex(midfloat.sty) = %{tl_version}, tex(stabular.sty) = %{tl_version}
Provides:       tex(stfloats.sty) = %{tl_version}, tex(texsort.sty) = %{tl_version}

%description -n texlive-sttools
A collection of tools and macros, providing: miscellaneous
float control, page styles for floats, multipage tabulars, even
columns at end of twocolumn region, switching between one- and
two-column anywhere, getting more mileage from \marginpar,
simulating the effect of "midfloats", a package to manipulate
numerical lists and arrays.

%package -n texlive-sttools-doc
Summary:        Documentation for sttools
Version:        svn43684
Provides:       tex-sttools-doc
AutoReqProv:    No

%description -n texlive-sttools-doc
Documentation for sttools

%package -n texlive-stubs
Provides:       tex-stubs = %{tl_version}
License:        GPL+
Summary:        Create tear-off stubs at the bottom of a page
Version:        svn19440.0.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(textpos.sty), tex(graphicx.sty)
Provides:       tex(stubs.sty) = %{tl_version}

%description -n texlive-stubs
The \stubs command creates as many repetitions as possible of
its argument, at the bottom of the page; these stubs may be
used (for example) for contact information.

%package -n texlive-stubs-doc
Summary:        Documentation for stubs
Version:        svn19440.0.1.1

Provides:       tex-stubs-doc
AutoReqProv:    No

%description -n texlive-stubs-doc
Documentation for stubs

%package -n texlive-subdepth
Provides:       tex-subdepth = %{tl_version}
License:        LPPL
Summary:        Unify maths subscript height
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(subdepth.sty) = %{tl_version}

%description -n texlive-subdepth
This package is based on code (posted long ago to comp.text.tex
by Donald Arseneau) to equalise the height of subscripts in
maths. The default behaviour is to place subscripts slightly
lower when there is a superscript as well, but this can look
odd in some situations.

%package -n texlive-subdepth-doc
Summary:        Documentation for subdepth
Version:        svn15878.0.1

Provides:       tex-subdepth-doc
AutoReqProv:    No

%description -n texlive-subdepth-doc
Documentation for subdepth

%package -n texlive-subeqn
Provides:       tex-subeqn = %{tl_version}
License:        LPPL
Summary:        Package for subequation numbering
Version:        svn15878.2.0b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(subeqn.sty) = %{tl_version}

%description -n texlive-subeqn
Sometimes it is necessary to be able to refer to subexpressions
of an equation. In order to do that these subexpressions should
be numbered. In standard LaTeX there is no provision for this.
To solve this problem Stephen Gildea once wrote subeqn.sty for
LaTeX 2.09; Donald Arsenau rewrote the macros and Johannes
Braams made them available for LaTeX2e. Note that this package
is not compatible with the package subeqnarray (written by
Johannes Braams), but it can be used together with the LaTeX
class options leqno and fleqn.

%package -n texlive-subeqn-doc
Summary:        Documentation for subeqn
Version:        svn15878.2.0b

Provides:       tex-subeqn-doc
AutoReqProv:    No

%description -n texlive-subeqn-doc
Documentation for subeqn

%package -n texlive-subeqnarray
Provides:       tex-subeqnarray = %{tl_version}
License:        LPPL
Summary:        Equation array with sub numbering
Version:        svn15878.2.1c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(subeqnarray.sty) = %{tl_version}

%description -n texlive-subeqnarray
This package defines the subeqnarray and subeqnarray*
environments, which behave like the corresponding eqnarray and
eqnarray* environments, except that the individual lines are
numbered like 1a, 1b, 1c, etc. To refer to these numbers an
extra label command \slabel is provided. Users are urged to
consider the alignment capabilities of the amsmath bundle,
which produce better results than eqnarray-related macros.

%package -n texlive-subeqnarray-doc
Summary:        Documentation for subeqnarray
Version:        svn15878.2.1c

Provides:       tex-subeqnarray-doc
AutoReqProv:    No

%description -n texlive-subeqnarray-doc
Documentation for subeqnarray

%package -n texlive-subfigmat
Provides:       tex-subfigmat = %{tl_version}
License:        LPPL
Summary:        Automates layout when using the subfigure package
Version:        svn20308.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(subfigure.sty)
Provides:       tex(subfigmat.sty) = %{tl_version}

%description -n texlive-subfigmat
Defines an array/matrix-type environment that is used with the
subfigure package to automate the placement of subfigures (or
tables or text). The subfigures are placed left-to-right, top-
to-bottom.

%package -n texlive-subfigmat-doc
Summary:        Documentation for subfigmat
Version:        svn20308.1.0

Provides:       tex-subfigmat-doc
AutoReqProv:    No

%description -n texlive-subfigmat-doc
Documentation for subfigmat

%package -n texlive-subfigure
Provides:       tex-subfigure = %{tl_version}
License:        LPPL
Summary:        Deprecated: Figures divided into subfigures
Version:        svn15878.2.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(subfigure.cfg) = %{tl_version}, tex(subfigure.sty) = %{tl_version}

%description -n texlive-subfigure
Provides support for the manipulation and reference of small or
'sub' figures and tables within a single figure or table
environment. It is convenient to use this package when your
subfigures are to be separately captioned, referenced, or are
to be included in the List-of-Figures. A new \subfigure command
is introduced which can be used inside a figure environment for
each subfigure. An optional first argument is used as the
caption for that subfigure. The package is now considered
obsolete: it was superseded by subfig, but users may find the
more recent subcaption package more satisfactory.

%package -n texlive-subfigure-doc
Summary:        Documentation for subfigure
Version:        svn15878.2.1.5

Provides:       tex-subfigure-doc
AutoReqProv:    No

%description -n texlive-subfigure-doc
Documentation for subfigure

%package -n texlive-subfiles
Provides:       tex-subfiles = %{tl_version}
License:        LPPL 1.3
Summary:        Individual typesetting of subfiles of a "main" document
Version:        svn48323
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(verbatim.sty)
Provides:       tex(subfiles.cls) = %{tl_version}, tex(subfiles.sty) = %{tl_version}

%description -n texlive-subfiles
Using subfiles the user can handle multi-file projects more
comfortably making it possible to both process the subsidiary
files by themselves and to process the main file that includes
them, without making any changes to either.

%package -n texlive-subfiles-doc
Summary:        Documentation for subfiles
Version:        svn48323
Provides:       tex-subfiles-doc
AutoReqProv:    No

%description -n texlive-subfiles-doc
Documentation for subfiles

%package -n texlive-subfloat
Provides:       tex-subfloat = %{tl_version}
License:        LPPL
Summary:        Sub-numbering for figures and tables
Version:        svn29349.2.14

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(subfloat.sty) = %{tl_version}

%description -n texlive-subfloat
This package enables sub-numbering of floats (figures and
tables) similar to the subequations-environment of the amsmath
package. The subfloat package is not to be confused with the
subfig package which generates sub-figures within one normal
figure, and manages their placement; subfloat only affects
captions and numbering.

%package -n texlive-subfloat-doc
Summary:        Documentation for subfloat
Version:        svn29349.2.14

Provides:       tex-subfloat-doc
AutoReqProv:    No

%description -n texlive-subfloat-doc
Documentation for subfloat

%package -n texlive-substitutefont
Provides:       tex-substitutefont = %{tl_version}
License:        LPPL 1.3
Summary:        Easy font substitution
Version:        svn32066.0.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(substitutefont.sty) = %{tl_version}

%description -n texlive-substitutefont
Many free fonts are extensions of a basic font family with new
glyphs or shapes. Such fonts may be given a new name due to
licence reasons or to the creator's preference. The package
facilitates the task of setting up a font family as substitute
for another one, using its \substitutefont command.

%package -n texlive-substitutefont-doc
Summary:        Documentation for substitutefont
Version:        svn32066.0.1.4

Provides:       tex-substitutefont-doc
AutoReqProv:    No

%description -n texlive-substitutefont-doc
Documentation for substitutefont

%package -n texlive-substr
Provides:       tex-substr = %{tl_version}
License:        LPPL
Summary:        Deal with substrings in strings
Version:        svn16117.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(substr.sty) = %{tl_version}

%description -n texlive-substr
The package provides commands to deal with substrings of
strings. Macros are provided to: determine if one string is a
substring of another, return the parts of a string before or
after a substring, and count the number of occurrences of a
substring.

%package -n texlive-substr-doc
Summary:        Documentation for substr
Version:        svn16117.1.2

Provides:       tex-substr-doc
AutoReqProv:    No

%description -n texlive-substr-doc
Documentation for substr

%package -n texlive-supertabular
Provides:       tex-supertabular = %{tl_version}
License:        LPPL 1.3
Summary:        A multi-page tables package
Version:        svn15878.4.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(supertabular.sty) = %{tl_version}

%description -n texlive-supertabular
The package was a predecessor of longtable; the newer package
(designed on quite different principles) is easier to use and
more flexible, in many cases, but supertabular retains its
usefulness in a few situations where longtable has problems.

%package -n texlive-supertabular-doc
Summary:        Documentation for supertabular
Version:        svn15878.4.1a

Provides:       tex-supertabular-doc
AutoReqProv:    No

%description -n texlive-supertabular-doc
Documentation for supertabular

%package -n texlive-svg
Provides:       tex-svg = %{tl_version}
License:        LPPL 1.3
Summary:        Include and extract SVG pictures using Inkscape
Version:        svn45941
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(subfig.sty), tex(import.sty), tex(graphicx.sty)
Requires:       tex(transparent.sty), tex(xcolor.sty)
Provides:       tex(svg.sty) = %{tl_version}

%description -n texlive-svg
The package provides a command similar to \includegraphics
command of the graphicx package, which enables the inclusion of
SVG images using Inkscape. \includesvg[<options>]{<svg
filename>} A variety of options is available, including width,
height, and path of the SVG. The image is converted to an
appropriate format, using the \write18 mechanism to execute a
shell command, and the package also offers the means of saving
a PDF, EPS, or PNG copy of the image, at the same time. The
documentation shows an example using an SVG created from the
high energy particle physics analysis package ROOT.

%package -n texlive-svg-doc
Summary:        Documentation for svg
Version:        svn45941
Provides:       tex-svg-doc
AutoReqProv:    No

%description -n texlive-svg-doc
Documentation for svg

%package -n texlive-svgcolor
Provides:       tex-svgcolor = %{tl_version}
License:        LPPL
Summary:        Define SVG named colours
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(svgcolor.sty) = %{tl_version}

%description -n texlive-svgcolor
The package defines the W3C Scalable Vector Graphics (SVG)
colour names for use with both the color and PSTricks packages.

%package -n texlive-svgcolor-doc
Summary:        Documentation for svgcolor
Version:        svn15878.1.0

Provides:       tex-svgcolor-doc
AutoReqProv:    No

%description -n texlive-svgcolor-doc
Documentation for svgcolor

%package -n texlive-svn
Provides:       tex-svn = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset Subversion keywords
Version:        svn15878.43

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(svn.sty) = %{tl_version}

%description -n texlive-svn
The svn package lets you typeset (in LaTeX) the value of
Subversion keywords. It is approximately an equivalent to the
rcs package, but for Subversion rather than CVS. Details of
Subversion (a replacement for CVS) is available from the
project's home site.

%package -n texlive-svn-doc
Summary:        Documentation for svn
Version:        svn15878.43

Provides:       tex-svn-doc
AutoReqProv:    No

%description -n texlive-svn-doc
Documentation for svn

%package -n texlive-svninfo
Provides:       tex-svninfo = %{tl_version}
License:        LPPL
Summary:        Typeset Subversion keywords
Version:        svn17554.0.7.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fancyheadings.sty), tex(fancyhdr.sty)
Requires:       tex(scrpage2.sty), tex(eso-pic.sty), tex(ifthen.sty)
Provides:       tex(svninfo.cfg) = %{tl_version}, tex(svninfo.sty) = %{tl_version}

%description -n texlive-svninfo
A package for incorporating the values of Subversion keywords
into typeset documents. Information about Subversion (a
replacement for CVS) is available from
http://subversion.tigris.org/

%package -n texlive-svninfo-doc
Summary:        Documentation for svninfo
Version:        svn17554.0.7.4

Provides:       tex-svninfo-doc
AutoReqProv:    No

%description -n texlive-svninfo-doc
Documentation for svninfo

%package -n texlive-svn-prov
Provides:       tex-svn-prov = %{tl_version}
License:        LPPL
Summary:        Subversion variants of \Provides... macros
Version:        svn18017.3.1862

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(svn-prov.sty) = %{tl_version}

%description -n texlive-svn-prov
The package introduces Subversion variants of the standard
LaTeX macros \ProvidesPackage, \ProvidesClass and \ProvidesFile
where the file name and date is extracted from Subversion Id
keywords. The file name may also be given explicitly as an
optional argument.

%package -n texlive-svn-prov-doc
Summary:        Documentation for svn-prov
Version:        svn18017.3.1862

Provides:       tex-svn-prov-doc
AutoReqProv:    No

%description -n texlive-svn-prov-doc
Documentation for svn-prov

%package -n texlive-syntax
Provides:       tex-syntax = %{tl_version}
License:        GPL+
Summary:        Creation of syntax diagrams
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(syntax.tex) = %{tl_version}

%description -n texlive-syntax
Create syntax diagrams using special environments and commands
to represent the diagram structure.

%package -n texlive-syntax-doc
Summary:        Documentation for syntax
Version:        svn15878.0

Provides:       tex-syntax-doc
AutoReqProv:    No

%description -n texlive-syntax-doc
Documentation for syntax

%package -n texlive-syntrace
Provides:       tex-syntrace = %{tl_version}
License:        LPPL
Summary:        Labels for tracing in a syntax tree
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(synttree.sty), tex(qtree.sty)
Provides:       tex(syntrace.sty) = %{tl_version}

%description -n texlive-syntrace
This package adds support for traces in trees created using
either the synttree or the qtree package. The package provides
two commands (\traceLabel and \traceReference) to set and use a
trace.

%package -n texlive-syntrace-doc
Summary:        Documentation for syntrace
Version:        svn15878.1.1

Provides:       tex-syntrace-doc
AutoReqProv:    No

%description -n texlive-syntrace-doc
Documentation for syntrace

%package -n texlive-synttree
Provides:       tex-synttree = %{tl_version}
License:        LPPL
Summary:        Typeset syntactic trees
Version:        svn16252.1.4.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(synttree.sty) = %{tl_version}

%description -n texlive-synttree
A package to typeset syntactic trees such as those used in
Chomsky's Generative grammar, based on a description of the
structure of the tree.

%package -n texlive-synttree-doc
Summary:        Documentation for synttree
Version:        svn16252.1.4.2

Provides:       tex-synttree-doc
AutoReqProv:    No

%description -n texlive-synttree-doc
Documentation for synttree

%package -n texlive-showhyphens
Provides:       tex-showhyphens = %{tl_version}
License:        MIT
Summary:        Show all possible hyphenations in LuaLaTeX
Version:        svn39787

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(luatexbase.sty)
Provides:       tex(showhyphens.sty) = %{tl_version}

%description -n texlive-showhyphens
With this package, LuaLaTeX will indicate all possible
hyphenations in the printed output.

%package -n texlive-showhyphens-doc
Summary:        Documentation for showhyphens
Version:        svn39787

Provides:       tex-showhyphens-doc
AutoReqProv:    No

%description -n texlive-showhyphens-doc
Documentation for showhyphens

%package -n texlive-spelling
Provides:       tex-spelling = %{tl_version}
License:        LPPL 1.3
Summary:        Support for spell-checking of LuaTeX documents
Version:        svn30715.0.41

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifluatex.sty), tex(luatexbase-modutils.sty)
Requires:       tex(luatexbase-mcb.sty), tex(luatexbase-attr.sty)
Requires:       tex(atbegshi.sty)
Provides:       tex(spelling.sty) = %{tl_version}

%description -n texlive-spelling
The package aids spell-checking of TeX documents compiled with
the LuaTeX engine. It can give visual feedback in PDF output
similar to WYSIWYG word processors. The package relies on an
external spell-checker application to check spelling of a text
file and to output a list of bad spellings. The package should
work with most spell-checkers, even dumb, TeX-unaware ones.

%package -n texlive-spelling-doc
Summary:        Documentation for spelling
Version:        svn30715.0.41

Provides:       tex-spelling-doc
AutoReqProv:    No

%description -n texlive-spelling-doc
Documentation for spelling

%package -n texlive-shuffle
Provides:       tex-shuffle = %{tl_version}
License:        Public Domain
Summary:        A symbol for the shuffle product
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(shuffle10.tfm) = %{tl_version}, tex(shuffle7.tfm) = %{tl_version}
Provides:       tex(Ushuffle.fd) = %{tl_version}, tex(shuffle.sty) = %{tl_version}

%description -n texlive-shuffle
The bundle provides a LaTeX package and a font (as Metafont
source) for the shuffle product which is used in some part of
mathematics and physics.

%package -n texlive-shuffle-doc
Summary:        Documentation for shuffle
Version:        svn15878.1.0

Provides:       tex-shuffle-doc
AutoReqProv:    No

%description -n texlive-shuffle-doc
Documentation for shuffle

%package -n texlive-skmath
Provides:       tex-skmath = %{tl_version}
License:        LPPL 1.3
Summary:        Extensions to the maths command repertoir
Version:        svn42902
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(l3keys2e.sty), tex(xparse.sty), tex(amssymb.sty)
Requires:       tex(mathtools.sty), tex(xfrac.sty), tex(isomath.sty)
Provides:       tex(skmath.sty) = %{tl_version}

%description -n texlive-skmath
The package provides a selection of new maths commands and
improved re-definitions of existing commands.

%package -n texlive-skmath-doc
Summary:        Documentation for skmath
Version:        svn42902
Provides:       tex-skmath-doc
AutoReqProv:    No

%description -n texlive-skmath-doc
Documentation for skmath

%package -n texlive-statex
Provides:       tex-statex = %{tl_version}
License:        LPPL
Summary:        Statistics style
Version:        svn20306.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(amsmath.sty), tex(amssymb.sty), tex(bm.sty)
Requires:       tex(color.sty)
Provides:       tex(statex.sty) = %{tl_version}

%description -n texlive-statex
A package defining many macros for items of significance in
statistical presentations. An updated, but incompatible,
version of the package is available: statex2.

%package -n texlive-statex-doc
Summary:        Documentation for statex
Version:        svn20306.1.6

Provides:       tex-statex-doc
AutoReqProv:    No

%description -n texlive-statex-doc
Documentation for statex

%package -n texlive-statex2
Provides:       tex-statex2 = %{tl_version}
License:        LPPL
Summary:        Statistics style
Version:        svn23961.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(amsmath.sty), tex(amssymb.sty), tex(bm.sty)
Requires:       tex(color.sty)
Provides:       tex(statex2.sty) = %{tl_version}

%description -n texlive-statex2
The package defines many macros for items of significance in
statistical presentations. It represents a syntax-incompatible
upgrade of statex.

%package -n texlive-statex2-doc
Summary:        Documentation for statex2
Version:        svn23961.2.1

Provides:       tex-statex2-doc
AutoReqProv:    No

%description -n texlive-statex2-doc
Documentation for statex2

%package -n texlive-subsupscripts
Provides:       tex-subsupscripts = %{tl_version}
License:        LPPL
Summary:        A range of sub- and superscript commands
Version:        svn16080.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(subsupscripts.sty) = %{tl_version}

%description -n texlive-subsupscripts
The package provides a comprehensive and flexible set of
commands for combinations of left and right sub- and
superscripts.

%package -n texlive-subsupscripts-doc
Summary:        Documentation for subsupscripts
Version:        svn16080.1.0

Provides:       tex-subsupscripts-doc
AutoReqProv:    No

%description -n texlive-subsupscripts-doc
Documentation for subsupscripts

%package -n texlive-susy
Provides:       tex-susy = %{tl_version}
License:        LPPL
Summary:        Macros for SuperSymmetry-related work
Version:        svn19440.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(susy.sty) = %{tl_version}

%description -n texlive-susy
The package provides abbreviations of longer expressions.

%package -n texlive-susy-doc
Summary:        Documentation for susy
Version:        svn19440.0

Provides:       tex-susy-doc
AutoReqProv:    No

%description -n texlive-susy-doc
Documentation for susy

%package -n texlive-syllogism
Provides:       tex-syllogism = %{tl_version}
License:        LPPL
Summary:        Typeset syllogisms in LaTeX
Version:        svn15878.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(amssymb.sty), tex(ifthen.sty), tex(xspace.sty)
Provides:       tex(syllogism.sty) = %{tl_version}

%description -n texlive-syllogism
The package provides a simple, configurable, way for neatly
typesetting syllogisms and syllogistic-like arguments, composed
of two premises and a conclusion.

%package -n texlive-syllogism-doc
Summary:        Documentation for syllogism
Version:        svn15878.1.2

Provides:       tex-syllogism-doc
AutoReqProv:    No

%description -n texlive-syllogism-doc
Documentation for syllogism

%package -n texlive-sympytexpackage
Provides:       tex-sympytexpackage = %{tl_version}
License:        LPPL
Summary:        sympytexpackage package
Version:        svn45818
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(verbatim.sty), tex(graphicx.sty), tex(makecmds.sty), tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(sympytex.sty) = %{tl_version}

%description -n texlive-sympytexpackage
sympytexpackage package

%package -n texlive-sympytexpackage-doc
Summary:        Documentation for sympytexpackage
Version:        svn45818
Provides:       tex-sympytexpackage-doc
AutoReqProv:    No

%description -n texlive-sympytexpackage-doc
Documentation for sympytexpackage

%package -n texlive-synproof
Provides:       tex-synproof = %{tl_version}
License:        LPPL
Summary:        Easy drawing of syntactic proofs
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(pstricks.sty), tex(pst-node.sty), tex(keyval.sty)
Provides:       tex(synproof.sty) = %{tl_version}

%description -n texlive-synproof
The package provides a set of macros based on PSTricks that
will enable you to draw syntactic proofs easily (inspired by
the Gamut books). Very few commands are needed, however fine
tuning of the various parameters (dimensions) can still be
achieved through "key=value" pairs.

%package -n texlive-synproof-doc
Summary:        Documentation for synproof
Version:        svn15878.1.0

Provides:       tex-synproof-doc
AutoReqProv:    No

%description -n texlive-synproof-doc
Documentation for synproof

%package -n texlive-soton
Provides:       tex-soton = %{tl_version}
License:        LPPL
Summary:        University of Southampton-compliant slides
Version:        svn16215.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xcolor.sty)
Provides:       tex(soton-beamer.sty) = %{tl_version}, tex(soton-palette.sty) = %{tl_version}

%description -n texlive-soton
The bundle contains two packages: soton-palette which defines
colour-ways, and soton-beamer, which uses the colours to
produce compliant presentations.

%package -n texlive-soton-doc
Summary:        Documentation for soton
Version:        svn16215.0.1

Provides:       tex-soton-doc
AutoReqProv:    No

%description -n texlive-soton-doc
Documentation for soton

%package -n texlive-sphdthesis
Provides:       tex-sphdthesis = %{tl_version}
License:        Public Domain
Summary:        Latex template for writing PhD Thesis
Version:        svn34374.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(fontenc.sty), tex(microtype.sty), tex(fix-cm.sty)
Requires:       tex(caption.sty), tex(graphicx.sty), tex(subfig.sty), tex(amsmath.sty)
Requires:       tex(amssymb.sty), tex(amsthm.sty), tex(float.sty), tex(xcolor.sty)
Requires:       tex(ifthen.sty), tex(geometry.sty), tex(emptypage.sty), tex(parskip.sty)
Requires:       tex(setspace.sty), tex(booktabs.sty), tex(colortbl.sty), tex(tabularx.sty)
Requires:       tex(algorithm2e.sty), tex(fancyhdr.sty), tex(tocloft.sty), tex(fncychap.sty)
Requires:       tex(sectsty.sty), tex(etoolbox.sty), tex(url.sty), tex(hyperref.sty)
Requires:       tex(cleveref.sty)
Provides:       tex(SPhdThesis.cls) = %{tl_version}

%description -n texlive-sphdthesis
The package provides a LaTeX document class for writing a PhD
thesis. The author developed it while writing his PhD thesis in
School of Computing (SoC), National University of Singapore
(NUS). By default, the class adheres to the NUS Guidelines on
Format of Research Thesis Submitted For Examination. However,
the class for conformation to a different guideline should not
be difficult.

%package -n texlive-sphdthesis-doc
Summary:        Documentation for sphdthesis
Version:        svn34374.1.0

Provides:       tex-sphdthesis-doc
AutoReqProv:    No

%description -n texlive-sphdthesis-doc
Documentation for sphdthesis

%package -n texlive-spie
Provides:       tex-spie = %{tl_version}
License:        LPPL
Summary:        Support for formatting SPIE Proceedings manuscripts
Version:        svn15878.3.25

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(cite.sty)
Provides:       tex(spie.cls) = %{tl_version}

%description -n texlive-spie
A class and a BibTeX style are provided.

%package -n texlive-spie-doc
Summary:        Documentation for spie
Version:        svn15878.3.25

Provides:       tex-spie-doc
AutoReqProv:    No

%description -n texlive-spie-doc
Documentation for spie

%package -n texlive-sr-vorl
Provides:       tex-sr-vorl = %{tl_version}
License:        LPPL 1.3
Summary:        Class for Springer books
Version:        svn39529

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(etoolbox.sty), tex(babel.sty), tex(geometry.sty)
Requires:       tex(scrpage2.sty), tex(caption.sty), tex(ragged2e.sty), tex(enumitem.sty)
Requires:       tex(xstring.sty), tex(chngcntr.sty), tex(onlyamsmath.sty), tex(microtype.sty)
Provides:       tex(sr-vorl.cls) = %{tl_version}

%description -n texlive-sr-vorl
The class provides a template for books to be published at
Springer Gabler, Vieweg or Springer Research. It may be used to
produce monographs in different formats and "several-authors-
books" fitting the conditions of Springer Gabler, Vieweg and
Springer Research.

%package -n texlive-sr-vorl-doc
Summary:        Documentation for sr-vorl
Version:        svn39529

Provides:       tex-sr-vorl-doc
AutoReqProv:    No

%description -n texlive-sr-vorl-doc
Documentation for sr-vorl

%package -n texlive-stellenbosch
Provides:       tex-stellenbosch = %{tl_version}
License:        LPPL
Summary:        Stellenbosch thesis bundle
Version:        svn36696.11a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(natbib.sty), tex(calc.sty), tex(array.sty), tex(longtable.sty)
Requires:       tex(colortbl.sty), tex(ifpdf.sty), tex(ifthen.sty), tex(keyval.sty)
Provides:       tex(usbib.sty) = %{tl_version}, tex(usnomencl.sty) = %{tl_version}
Provides:       tex(ussummary.sty) = %{tl_version}, tex(usthesis.cls) = %{tl_version}
Provides:       tex(usthesis.sty) = %{tl_version}, tex(ustitle.sty) = %{tl_version}

%description -n texlive-stellenbosch
The usthesis class/style files are provided to typeset reports,
theses and dissertations that conform to the requirements of
the Engineering Faculty of the University of Stellenbosch. The
class file usthesis.cls is based on the standard LaTeX book
class, while usthesis.sty is a style file to be loaded on top
of the very powerful memoir class. Both options give identical
output, but the benefit of the using memoir is that it has many
additional command and environments for formatting and
processing of a document. Usthesis is primarily concerned with
the formatting of the front matter such as the title page,
abstract, etc. and a decent page layout on A4 paper. It also
works together with the babel package to provide language
options to typeset documents in Afrikaans or in English.
Additional packages are provided for bibliographic matter, note
title pages, lists of symbols, as well as various graphic files
for logos.

%package -n texlive-stellenbosch-doc
Summary:        Documentation for stellenbosch
Version:        svn36696.11a

Provides:       tex-stellenbosch-doc
AutoReqProv:    No

%description -n texlive-stellenbosch-doc
Documentation for stellenbosch

%package -n texlive-suftesi
Provides:       tex-suftesi = %{tl_version}
License:        LPPL 1.3
Summary:        A document class for typesetting theses, books and articles
Version:        svn40238

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(geometry.sty), tex(enumitem.sty), tex(caption.sty)
Requires:       tex(color.sty), tex(multicol.sty), tex(emptypage.sty), tex(textcase.sty)
Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(ifthen.sty), tex(microtype.sty)
Requires:       tex(cclicenses.sty), tex(fontenc.sty), tex(substitutefont.sty), tex(lmodern.sty)
Requires:       tex(mathpazo.sty), tex(beramono.sty), tex(crop.sty), tex(titlesec.sty)
Requires:       tex(extramarks.sty), tex(fancyhdr.sty), tex(titletoc.sty), tex(fixltxhyph.sty)
Provides:       tex(suftesi.cls) = %{tl_version}

%description -n texlive-suftesi
The class is specifically designed for use with theses in the
humanities.

%package -n texlive-suftesi-doc
Summary:        Documentation for suftesi
Version:        svn40238

Provides:       tex-suftesi-doc
AutoReqProv:    No

%description -n texlive-suftesi-doc
Documentation for suftesi

%package -n texlive-sugconf
Provides:       tex-sugconf = %{tl_version}
License:        LPPL
Summary:        SAS(R) user group conference proceedings document class
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(sugconf.cls) = %{tl_version}

%description -n texlive-sugconf
The class may be used to typeset articles to be published in
the proceedings of SAS(R) User group conferences and workshops.
The layout produced by the class is based on that published by
SAS Institute (2006).

%package -n texlive-sugconf-doc
Summary:        Documentation for sugconf
Version:        svn15878.0

Provides:       tex-sugconf-doc
AutoReqProv:    No

%description -n texlive-sugconf-doc
Documentation for sugconf

%package -n texlive-siunitx
Provides:       tex-siunitx = %{tl_version}
License:        LPPL 1.3
Summary:        A comprehensive (SI) units package
Version:        svn47746
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(amstext.sty), tex(array.sty)
Requires:       tex(l3keys2e.sty), tex(xspace.sty), tex(translator.sty)
Provides:       tex(siunitx-abbreviations.cfg) = %{tl_version}
Provides:       tex(siunitx-binary.cfg) = %{tl_version}, tex(siunitx-version-1.cfg) = %{tl_version}
Provides:       tex(siunitx.sty) = %{tl_version}

%description -n texlive-siunitx
Typesetting values with units requires care to ensure that the
combined mathematical meaning of the value plus unit
combination is clear. In particular, the SI units system lays
down a consistent set of units with rules on how they are to be
used. However, different countries and publishers have
differing conventions on the exact appearance of numbers (and
units). A number of LaTeX packages have been developed to
provide consistent application of the various rules: SIunits,
sistyle, unitsdef and units are the leading examples. The
numprint package provides a large number of number-related
functions, while dcolumn and rccol provide tools for
typesetting tabular numbers. The siunitx package takes the best
from the existing packages, and adds new features and a
consistent interface. A number of new ideas have been
incorporated, to fill gaps in the existing provision. The
package also provides backward-compatibility with SIunits,
sistyle, unitsdef and units. The aim is to have one package to
handle all of the possible unit-related needs of LaTeX users.
The package relies on LaTeX 3 support from the l3kernel and
l3packages bundles.

%package -n texlive-siunitx-doc
Summary:        Documentation for siunitx
Version:        svn47746
Provides:       tex-siunitx-doc
AutoReqProv:    No

%description -n texlive-siunitx-doc
Documentation for siunitx

%package -n texlive-steinmetz
Provides:       tex-steinmetz = %{tl_version}
License:        LPPL
Summary:        Print Steinmetz notation
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pict2e.sty)
Provides:       tex(steinmetz.sty) = %{tl_version}

%description -n texlive-steinmetz
The steinmetz package provides a command for typesetting
complex numbers in the Steinmetz notation used in
electrotechnics as: <modulus>;<argument or phase inside an
angle symbol> The package makes use of pict2e.

%package -n texlive-steinmetz-doc
Summary:        Documentation for steinmetz
Version:        svn15878.1.0

Provides:       tex-steinmetz-doc
AutoReqProv:    No

%description -n texlive-steinmetz-doc
Documentation for steinmetz

%package -n texlive-struktex
Provides:       tex-struktex = %{tl_version}
License:        LPPL 1.2
Summary:        Draw Nassi-Schneidermann charts
Version:        svn47931
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifpdf.sty), tex(hyperref.sty), tex(color.sty), tex(nameref.sty)
Requires:       tex(url.sty), tex(ifthen.sty), tex(struktxp.sty), tex(curves.sty)
Requires:       tex(pict2e.sty)
Provides:       tex(strukdoc.sty) = %{tl_version}, tex(struktex.sty) = %{tl_version}
Provides:       tex(struktxf.sty) = %{tl_version}, tex(struktxp.sty) = %{tl_version}

%description -n texlive-struktex
Even in the age of OOP one must develop algorithms. Nassi-
Shneiderman diagrams are a well known tool to describe an
algorithm in a graphical way. The package offers some macros
for generating those diagrams in a LaTeX document. The package
provides the most important elements of a Nassi-Shneiderman
diagram, including processing blocks, loops, mapping
conventions for alternatives, etc. Diagrams are drawn using the
picture environment (using pict2e for preference).

%package -n texlive-struktex-doc
Summary:        Documentation for struktex
Version:        svn47931
Provides:       tex-struktex-doc
AutoReqProv:    No

%description -n texlive-struktex-doc
Documentation for struktex

%package -n texlive-substances
Provides:       tex-substances = %{tl_version}
License:        LPPL 1.3
Summary:        A database of chemicals
Version:        svn40989

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(xtemplate.sty)
Requires:       tex(chemmacros.sty)
Provides:       tex(substances-default.def) = %{tl_version}
Provides:       tex(substances.sty) = %{tl_version}

%description -n texlive-substances
The package provides the means to create a database-like file
that contains data of various chemicals. These data may be
retrieved in the document; an index of the chemicals mentioned
in the document can be created..

%package -n texlive-substances-doc
Summary:        Documentation for substances
Version:        svn40989

Provides:       tex-substances-doc
AutoReqProv:    No

%description -n texlive-substances-doc
Documentation for substances

%package -n texlive-signchart-doc
Provides:       tex-signchart-doc = %{tl_version}
License:        LPPL
Summary:        doc files of signchart
Version:        svn39707

AutoReqProv:    No

%description -n texlive-signchart-doc
Documentation for signchart

%package -n texlive-signchart
Provides:       tex-signchart = %{tl_version}
License:        LPPL
Summary:        Create beautifully typeset sign charts
Version:        svn39707

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(signchart.sty) = %{tl_version}

%description -n texlive-signchart
The package allows users to easily typeset beautiful looking
sign charts directly into their (La)TeX document.

%package -n texlive-simpler-wick-doc
Provides:       tex-simpler-wick-doc = %{tl_version}
License:        GPLv3+
Summary:        doc files of simpler-wick
Version:        svn39074

AutoReqProv:    No

%description -n texlive-simpler-wick-doc
Documentation for simpler-wick

%package -n texlive-simpler-wick
Provides:       tex-simpler-wick = %{tl_version}
License:        LPPL
Summary:        Simpler Wick contractions
Version:        svn39074

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(simpler-wick.sty) = %{tl_version}

%description -n texlive-simpler-wick
In every quantum field theory course, there will be a chapter
about Wick's theorem and how it can be used to convert a very
large product of many creation and annihilation operators into
something more tractable and normal ordered. The contractions
are denoted with a square bracket over the operators which are
being contracted, which used to be rather annoying to typeset
in LaTeX as the only other package available was simplewick,
which is rather unwieldy. This package provides a simpler
syntax for Wick contractions.

%package -n texlive-svg-inkscape-doc
Summary:        Documentation for svg-inkscape
Version:        svn32199.0

Provides:       tex-svg-inkscape-doc
AutoReqProv:    No

%description -n texlive-svg-inkscape-doc
Documentation for svg-inkscape

%package -n texlive-smartunits-doc
Provides:       tex-smartunits-doc = %{tl_version}
License:        LPPL
Summary:        doc files of smartunits
Version:        svn39592

AutoReqProv:    No

%description -n texlive-smartunits-doc
Documentation for smartunits

%package -n texlive-smartunits
Provides:       tex-smartunits = %{tl_version}
License:        LPPL
Summary:        Converting between common metric and Imperial units
Version:        svn39592

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(smartunits.sty) = %{tl_version}

%description -n texlive-smartunits
This LaTeX package implements a \SmartUnit macro for converting
between (some) metric and Imperial units. The package requires
pgfkeys and siunitx.

%package -n texlive-swebib
Provides:       tex-swebib = %{tl_version}
License:        LPPL 1.2
Summary:        Swedish bibliography styles
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-swebib
The bundle contains Swedish versions of the standard
bibliography styles, and of the style plainnat. The styles
should be funtionally equivalent to the corresponding original
styles, apart from the Swedish translations. The styles do not
implement Swedish collation.

%package -n texlive-swebib-doc
Summary:        Documentation for swebib
Version:        svn15878.0

Provides:       tex-swebib-doc
AutoReqProv:    No

%description -n texlive-swebib-doc
Documentation for swebib

%package -n texlive-svrsymbols-doc
Provides:       tex-svrsymbols-doc = %{tl_version}
License:        LPPL
Summary:        doc files of svrsymbols
Version:        svn40371

AutoReqProv:    No

%description -n texlive-svrsymbols-doc
Documentation for svrsymbols

%package -n texlive-svrsymbols
Provides:       tex-svrsymbols = %{tl_version}
License:        LPPL
Summary:        'A new font with symbols for use in Physics texts.'
Version:        svn40371

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(svrsymbols.sty) = %{tl_version}, tex(svrsymbols.map) = %{tl_version}
Provides:       tex(SVRsymbols.pfb) = %{tl_version}, tex(SVRsymbols.tfm) = %{tl_version}

%description -n texlive-svrsymbols
The svrsymbols package is a LaTeX interface to theSVRsymbols
font. The glyphs of this font are ideograms that have been
designed for use in Physics texts. Some symbols are standard
and some are entirely new.

Version:        svn43291
AutoReqProv:    No

%package -n texlive-shobhika
Summary:        An OpenType Devanagari font designed for scholars
Version:        svn44723
License:        OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(Shobhika-Bold.otf) = %{tl_version}, tex(Shobhika-Regular.otf) = %{tl_version}

%description -n texlive-shobhika
This package provides a free, open source, Unicode compliant,
OpenType font with support for Devanagari, Latin, and Cyrillic
scripts. It is available in two weights--regular and bold. The
font is designed with over 1600 Devanagari glyphs, including
support for over 1100 conjunct consonants, as well as vedic
accents. The Latin component of the font not only supports a
wide range of characters required for Roman transliteration of
Sanskrit, but also provides a subset of regularly used
mathematical symbols for scholars working with scientific and
technical documents. The project has been launched under the
auspices of the Science and Heritage Initiative (SandHI) at IIT
Bombay, and builds upon the following two fonts for its
Devanagari and Latin components respectively: (i) Yashomudra by
Rajya Marathi Vikas Samstha, and (ii) PT Serif by ParaType. We
would like to thank both these organisations for releasing
their fonts under the SIL Open Font Licence, which has enabled
us to create Shobhika.

%package -n texlive-simple-resume-cv
Summary:        Template for a simple resume or curriculum vitae (CV), in XeLaTeX
Version:        svn43057
License:        Public Domain
Requires:       texlive-base texlive-kpathsea
Provides:       tex(simpleresumecv.cls) = %{tl_version}

%description -n texlive-simple-resume-cv
Template for a simple resume or curriculum vitae (CV), in
XeLaTeX. Simple template that can be further customized or
extended, with numerous examples.

%package -n texlive-simple-thesis-dissertation
Summary:        Template for a simple thesis or dissertation (Ph.D. or master's degree) or technical report, in XeLaTeX
Version:        svn43058
License:        Public Domain
Requires:       texlive-base texlive-kpathsea
Provides:       tex(simplethesisdissertation.cls) = %{tl_version}

%description -n texlive-simple-thesis-dissertation
Template for a simple thesis or dissertation (Ph.D. or master's
degree) or technical report, in XeLaTeX. Simple template that
can be further customized or extended, with numerous examples.
Consistent style for figures, tables, mathematical theorems,
definitions, lemmas, etc.

%package -n texlive-soup
Summary:        Generate alphabet soup puzzles
Version:        svn42992
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(soup.sty) = %{tl_version}

%description -n texlive-soup
Generate alphabet soup puzzles (aka word search puzzles), and
variations using numbers or other symbols. Provides macros to
generate an alphabet soup style puzzle (also known as word
search puzzles or "find-the-word" puzzles). Allow creating
numbersoup and soups with custom symbol sets.

%package -n texlive-spark-otf
Summary:        Support OpenType Spark fonts
Version:        svn45483
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(spark-otf.sty) = %{tl_version}

%description -n texlive-spark-otf
The package supports the free fonts from "After the Flood"
which are available from AtF Spark. The following fonts are
supported: Spark - Bar - Medium Spark - Bar - Narrow Spark -
Bar - Thin Spark - Dot-line - Medium Spark - Dot - Medium Spark
- Dot - Small

%package -n texlive-spectralsequences
Summary:        Print spectral sequence diagrams using PGF/TikZ
Version:        svn46038
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(spectralsequences.sty) = %{tl_version}
Provides:       tex(sseqcheckdefinitions.code.tex) = %{tl_version}
Provides:       tex(sseqdrawing.code.tex) = %{tl_version}
Provides:       tex(sseqforeach.code.tex) = %{tl_version}
Provides:       tex(sseqkeys.code.tex) = %{tl_version}, tex(sseqloadstore.code.tex) = %{tl_version}
Provides:       tex(sseqmacromakers.code.tex) = %{tl_version}
Provides:       tex(sseqmain.code.tex) = %{tl_version}, tex(sseqmessages.code.tex) = %{tl_version}
Provides:       tex(sseqparsers.code.tex) = %{tl_version}

%description -n texlive-spectralsequences
The package is a specialized tool built on top of PGF/TikZ for
drawing spectral sequences. It provides a powerful, concise
syntax for specifying the data of a spectral sequence, and then
allows the user to print various pages of spectral sequences,
automatically choosing which subset of the classes,
differentials, and structure lines to display on each page. It
also handles most of the details of the layout. At the same
time, it is extremely flexible. spectralsequences is closely
integrated with TikZ to ensure that users can take advantage of
as much as possible of its expressive power. It is possible to
turn off most of the automated layout features and draw
replacements using TikZ commands. The package also provides a
carefully designed error reporting system intended to ensure
that it is as clear as possible what is going wrong.

%package -n texlive-short-math-guide
Summary:        Guide to using amsmath and related packages to typeset mathematical notation with LaTeX
Version:        svn46126
License:        LPPL
Requires:       texlive-base texlive-kpathsea

%package -n texlive-studenthandouts
Summary:        Management and styling of student handout projects
Version:        svn43516
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(studenthandouts.sty) = %{tl_version}

%description -n texlive-studenthandouts
This package can be used to generate a single master document
that contains a set of individual student handouts. The package
has two main functions. First, it provides a simple framework
for organizing handout source code, and supplies a set of
import management tools for selectively importing a subset of
the handouts into the master document. Selective import is
convenient when compilation of all of the handouts is
unnecessary, for example when working on a new handout. As a
secondary feature, the package defines a basic visual style for
handouts. This style can be easily changed.

%package -n texlive-simplekv
Summary:        A simple key/value system for TeX and LaTeX
Version:        svn44987
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(simplekv.sty) = %{tl_version}, tex(simplekv.tex) = %{tl_version}

%description -n texlive-simplekv
The package provides a simple key/value system for TeX and
LaTeX.

%description -n texlive-short-math-guide
The Short Math Guide is intended to be a concise introduction
to the use of the facilities provided by amsmath and various
other LaTeX packages for typesetting mathematical notation.
Originally created by Michael Downes of the American
Mathematical Society based only on amsmath, it has been brought
up to date with references to related packages and other useful
information.

%package -n texlive-simpleinvoice
Summary:        Easy typesetting of invoices
Version:        svn45673
License:        GPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(simpleinvoice.sty) = %{tl_version}

%description -n texlive-simpleinvoice
This package lets you easily typeset professional-looking
invoices. The user specifies the content of the invoice by
different \setPROPERTY commands, and an invoice is generated
automatically with the \makeinvoice command.

%package -n texlive-spalign
Summary:        Typeset matrices and arrays with spaces and semicolons as delimiters
Version:        svn42225
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(spalign.sty) = %{tl_version}

%description -n texlive-spalign
Typeset matrices and arrays with spaces and semicolons as
delimiters. The purpose of this package is to decrease the
number of keystrokes needed to typeset small amounts of aligned
material (matrices, arrays, etc.). It provides a facility for
typing alignment environments and macros with spaces as the
alignment delimiter and semicolons (by default) as the
end-of-row indicator. For instance, typeset a matrix using
\spalignmat{1 12 -3; 24 -2 2; 0 0 1}, or a vector using
\spalignvector{22 \frac{1}{2} -14}. This package also contains
utility macros for typesetting augmented matrices, vectors,
arrays, systems of equations, and more, and is easily
extendable to other situations that use alignments. People who
have to typeset a large number of matrices (like linear algebra
teachers) should find this package to be a real time saver.

%package -n texlive-stanli
Summary:        TikZ Library for Structural Analysis
Version:        svn42765
License:        GPL+ and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(stanli.sty) = %{tl_version}

%description -n texlive-stanli
stanli is a STructural ANalysis LIbrary based on PGF/TikZ.
Creating new assignments and tests, at university, is usually a
very time-consuming task, especially when this includes drawing
graphics. In the field of structural engineering, those small
structures are a key part for teaching. This package permits to
create such 2D and 3D structures in a very fast and simple way.

%package -n texlive-statistics
Summary:        Compute and typeset statistics tables and graphics
Version:        svn48252
License:        GPLv3+
Requires:       texlive-base texlive-kpathsea
Provides:       tex(statistics.sty) = %{tl_version}

%description -n texlive-statistics
The 'statistics' package can compute and typeset statistics
like frequency tables, cumulative distribution functions
(increasing or decreasing, in frequency or absolute count
domain), from the counts of individual values, or ranges, or
even the raw value list with repetitions. It can also compute
and draw a bar diagram in case of individual values, or, when
the data repartition is known from ranges, an histogram or the
continuous cumulative distribution function. You can ask
'statistics' to display no result, selective results or all of
them. Similarly 'statistics' can draw only some parts of the
graphs. Every part of the generated tables or graphics is
customizable.

%package -n texlive-statmath
Summary:        A LaTeX package for simple use of statistical notation
Version:        svn46925
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(statmath.sty) = %{tl_version}

%description -n texlive-statmath
The package offers anumber of notational conventions to be used
in applied and theoretical papers in statistics which are
currently lacking in the popular amsmath package. The seasoned
LaTeX user will see that the provided commands are simple,
almost trivial, but will hopefully offer less cluttered
preambles as well as a welcome help for novice users.

%package -n texlive-stealcaps
Summary:        "Steal" small capitals
Version:        svn46434
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(pgfopts.sty)
Requires:       tex(iftex.sty), tex(fontspec.sty)
Provides:       tex(stealcaps.sty) = %{tl_version}

%description -n texlive-stealcaps
This little package is mainly meant to be used when there is a
(TrueType or OpenType) font that does not provide real small
capitals. As a workaround, this package helps to borrow, or
"steal", the small capitals from another font. This might also
be useful in the rare case that someone does not like the
present small capitals, and wants to change them, or likes
those from another font better. To achieve the borrowing, one
only needs to load the package and specify the name of the
target font via the from option. Package dependencies: pgfopts,
iftex, fontspec.

%package -n texlive-stickstoo
Summary:        A reworking of STIX2
Version:        svn47858
License:        OFL and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(SticksTooText-Bold.afm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic.afm) = %{tl_version}
Provides:       tex(SticksTooText-Italic.afm) = %{tl_version}
Provides:       tex(SticksTooText-Regular.afm) = %{tl_version}
Provides:       tex(stickstooMath-Bold.afm) = %{tl_version}
Provides:       tex(stickstooMath-BoldItalic.afm) = %{tl_version}
Provides:       tex(stickstooMath-Italic.afm) = %{tl_version}
Provides:       tex(stickstooMath-Regular.afm) = %{tl_version}
Provides:       tex(stx2-ot1.enc) = %{tl_version}, tex(stx2_3t3wpf.enc) = %{tl_version}
Provides:       tex(stx2_3vezss.enc) = %{tl_version}, tex(stx2_4fcdhj.enc) = %{tl_version}
Provides:       tex(stx2_57cumc.enc) = %{tl_version}, tex(stx2_5xzouo.enc) = %{tl_version}
Provides:       tex(stx2_7bhcze.enc) = %{tl_version}, tex(stx2_7fpfyw.enc) = %{tl_version}
Provides:       tex(stx2_ao4o3i.enc) = %{tl_version}, tex(stx2_b3i2vo.enc) = %{tl_version}
Provides:       tex(stx2_bg3hea.enc) = %{tl_version}, tex(stx2_btooep.enc) = %{tl_version}
Provides:       tex(stx2_c34sac.enc) = %{tl_version}, tex(stx2_dbm33u.enc) = %{tl_version}
Provides:       tex(stx2_eexofg.enc) = %{tl_version}, tex(stx2_eqh7z7.enc) = %{tl_version}
Provides:       tex(stx2_gbmh45.enc) = %{tl_version}, tex(stx2_gxpwoy.enc) = %{tl_version}
Provides:       tex(stx2_hfcbd6.enc) = %{tl_version}, tex(stx2_irreni.enc) = %{tl_version}
Provides:       tex(stx2_iximus.enc) = %{tl_version}, tex(stx2_m7frfq.enc) = %{tl_version}
Provides:       tex(stx2_nb7tts.enc) = %{tl_version}, tex(stx2_nl7rkm.enc) = %{tl_version}
Provides:       tex(stx2_noim42.enc) = %{tl_version}, tex(stx2_opxk4k.enc) = %{tl_version}
Provides:       tex(stx2_pu4fsw.enc) = %{tl_version}, tex(stx2_pwkoq7.enc) = %{tl_version}
Provides:       tex(stx2_qdtmbx.enc) = %{tl_version}, tex(stx2_quvxut.enc) = %{tl_version}
Provides:       tex(stx2_rejbux.enc) = %{tl_version}, tex(stx2_rfrl5v.enc) = %{tl_version}
Provides:       tex(stx2_sdn3a4.enc) = %{tl_version}, tex(stx2_slv267.enc) = %{tl_version}
Provides:       tex(stx2_srw4fv.enc) = %{tl_version}, tex(stx2_t6nmmd.enc) = %{tl_version}
Provides:       tex(stx2_tu2ozo.enc) = %{tl_version}, tex(stx2_uab2xo.enc) = %{tl_version}
Provides:       tex(stx2_uhazou.enc) = %{tl_version}, tex(stx2_uofyr3.enc) = %{tl_version}
Provides:       tex(stx2_v3a2cx.enc) = %{tl_version}, tex(stx2_vydqhu.enc) = %{tl_version}
Provides:       tex(stx2_w6fsfr.enc) = %{tl_version}, tex(stx2_wfth6k.enc) = %{tl_version}
Provides:       tex(stx2_wwmqdh.enc) = %{tl_version}, tex(stx2_wwolpm.enc) = %{tl_version}
Provides:       tex(stx2_wxq2z6.enc) = %{tl_version}, tex(stx2_y4oioo.enc) = %{tl_version}
Provides:       tex(stx2_ym7moh.enc) = %{tl_version}, tex(stx2_zscetg.enc) = %{tl_version}
Provides:       tex(stx2i-ot1.enc) = %{tl_version}, tex(SticksTooText.map) = %{tl_version}
Provides:       tex(SticksTooText-Bold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-numr-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-numr-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-th-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-th-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-th-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-numr-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-th-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-th-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-th-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-th-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-th-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-th-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-th-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-th-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-th-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-dnom-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-numr-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-numr-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-numr-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-numr-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-numr-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-ot1G.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(ntxstx2bmi.tfm) = %{tl_version}, tex(ntxstx2bmia.tfm) = %{tl_version}
Provides:       tex(ntxstx2mi.tfm) = %{tl_version}, tex(ntxstx2mia.tfm) = %{tl_version}
Provides:       tex(stickstooMath-Bold.tfm) = %{tl_version}
Provides:       tex(stickstooMath-BoldItalic.tfm) = %{tl_version}
Provides:       tex(stickstooMath-Italic.tfm) = %{tl_version}
Provides:       tex(stickstooMath-Regular.tfm) = %{tl_version}
Provides:       tex(SticksTooText-Bold.pfb) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic.pfb) = %{tl_version}
Provides:       tex(SticksTooText-Italic.pfb) = %{tl_version}
Provides:       tex(SticksTooText-Regular.pfb) = %{tl_version}
Provides:       tex(stickstooMath-Bold.pfb) = %{tl_version}
Provides:       tex(stickstooMath-BoldItalic.pfb) = %{tl_version}
Provides:       tex(stickstooMath-Italic.pfb) = %{tl_version}
Provides:       tex(stickstooMath-Regular.pfb) = %{tl_version}
Provides:       tex(SticksTooText-Bold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-dnom-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-numr-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-numr-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-numr-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-numr-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-dnom-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-th-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-th-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-numr-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-numr-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-th-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-th-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-th-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-th-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-th-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-th-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-dnom-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-dnom-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-inf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-numr-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-numr-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-sup-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-ot1G.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(SticksTooText-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(ntxstx2bmi.vf) = %{tl_version}, tex(ntxstx2bmia.vf) = %{tl_version}
Provides:       tex(ntxstx2mi.vf) = %{tl_version}, tex(ntxstx2mia.vf) = %{tl_version}
Provides:       tex(LY1SticksTooText-Dnom.fd) = %{tl_version}
Provides:       tex(LY1SticksTooText-Inf.fd) = %{tl_version}
Provides:       tex(LY1SticksTooText-LF.fd) = %{tl_version}
Provides:       tex(LY1SticksTooText-Numr.fd) = %{tl_version}
Provides:       tex(LY1SticksTooText-OsF.fd) = %{tl_version}
Provides:       tex(LY1SticksTooText-Sup.fd) = %{tl_version}
Provides:       tex(LY1SticksTooText-TLF.fd) = %{tl_version}
Provides:       tex(LY1SticksTooText-TOsF.fd) = %{tl_version}
Provides:       tex(OT1SticksTooText-Dnom.fd) = %{tl_version}
Provides:       tex(OT1SticksTooText-Inf.fd) = %{tl_version}
Provides:       tex(OT1SticksTooText-LF.fd) = %{tl_version}
Provides:       tex(OT1SticksTooText-Numr.fd) = %{tl_version}
Provides:       tex(OT1SticksTooText-OsF.fd) = %{tl_version}
Provides:       tex(OT1SticksTooText-Sup.fd) = %{tl_version}
Provides:       tex(OT1SticksTooText-TLF.fd) = %{tl_version}
Provides:       tex(OT1SticksTooText-TOsF.fd) = %{tl_version}
Provides:       tex(T1SticksTooText-Dnom.fd) = %{tl_version}
Provides:       tex(T1SticksTooText-Inf.fd) = %{tl_version}
Provides:       tex(T1SticksTooText-LF.fd) = %{tl_version}
Provides:       tex(T1SticksTooText-Numr.fd) = %{tl_version}
Provides:       tex(T1SticksTooText-OsF.fd) = %{tl_version}
Provides:       tex(T1SticksTooText-Sup.fd) = %{tl_version}
Provides:       tex(T1SticksTooText-TLF.fd) = %{tl_version}
Provides:       tex(T1SticksTooText-TOsF.fd) = %{tl_version}
Provides:       tex(TS1SticksTooText-LF.fd) = %{tl_version}
Provides:       tex(TS1SticksTooText-OsF.fd) = %{tl_version}
Provides:       tex(TS1SticksTooText-TLF.fd) = %{tl_version}
Provides:       tex(TS1SticksTooText-TOsF.fd) = %{tl_version}
Provides:       tex(stickstootext.sty) = %{tl_version}

%description -n texlive-stickstoo
SticksToo is a reworking of the STIX2 with support files
focussing on enhancements of support for LaTeX users wishing to
be able to access more of its features. A companion addition to
the newtxmath package (version 1.55) provides a matching math
package using STIX2 letters (Roman and Greek) with newtxmath
symbols.

%package -n texlive-stix2-otf
Summary:        OpenType Unicode text and maths fonts
Version:        svn47549
License:        OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(STIX2Math.otf) = %{tl_version}, tex(STIX2Text-Bold.otf) = %{tl_version}
Provides:       tex(STIX2Text-BoldItalic.otf) = %{tl_version}
Provides:       tex(STIX2Text-Italic.otf) = %{tl_version}
Provides:       tex(STIX2Text-Regular.otf) = %{tl_version}

%description -n texlive-stix2-otf
The Scientific and Technical Information eXchange (STIX) fonts
are intended to satisfy the demanding needs of authors,
publishers, printers, and others working in the scientific,
medical, and technical fields. They combine a comprehensive
Unicode-based collection of mathematical symbols and alphabets
with a set of text faces suitable for professional publishing.
The fonts are available royalty-free under the SIL Open Font
License.

%package -n texlive-stix2-type1
Summary:        Type1 versions of the STIX Two OpenType fonts
Version:        svn47554
License:        OFL and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(stix2-mathbb.enc) = %{tl_version}, tex(stix2-mathbbit.enc) = %{tl_version}
Provides:       tex(stix2-mathcal.enc) = %{tl_version}, tex(stix2-mathex.enc) = %{tl_version}
Provides:       tex(stix2-mathfrak-bold.enc) = %{tl_version}
Provides:       tex(stix2-mathfrak.enc) = %{tl_version}, tex(stix2-mathit-bold.enc) = %{tl_version}
Provides:       tex(stix2-mathit.enc) = %{tl_version}, tex(stix2-mathrm-bold.enc) = %{tl_version}
Provides:       tex(stix2-mathrm.enc) = %{tl_version}, tex(stix2-mathscr-bold.enc) = %{tl_version}
Provides:       tex(stix2-mathscr.enc) = %{tl_version}, tex(stix2-mathsf-bold.enc) = %{tl_version}
Provides:       tex(stix2-mathsf.enc) = %{tl_version}, tex(stix2-mathsfit-bold.enc) = %{tl_version}
Provides:       tex(stix2-mathsfit.enc) = %{tl_version}, tex(stix2-mathtt.enc) = %{tl_version}
Provides:       tex(stix2-ot1.enc) = %{tl_version}, tex(stix2-ot1sc.enc) = %{tl_version}
Provides:       tex(stix2-ot2.enc) = %{tl_version}, tex(stix2-ot2sc.enc) = %{tl_version}
Provides:       tex(stix2-t1.enc) = %{tl_version}, tex(stix2-t1sc.enc) = %{tl_version}
Provides:       tex(stix2-ts1.enc) = %{tl_version}, tex(stix2.map) = %{tl_version}
Provides:       tex(ot1-stix2text-bold.pl) = %{tl_version}
Provides:       tex(ot1-stix2text-bolditalic.pl) = %{tl_version}
Provides:       tex(ot1-stix2text-italic.pl) = %{tl_version}
Provides:       tex(ot1-stix2text.pl) = %{tl_version}, tex(ot1-stix2textsc-bold.pl) = %{tl_version}
Provides:       tex(ot1-stix2textsc.pl) = %{tl_version}, tex(ot2-stix2text-bold.pl) = %{tl_version}
Provides:       tex(ot2-stix2text-bolditalic.pl) = %{tl_version}
Provides:       tex(ot2-stix2text-italic.pl) = %{tl_version}
Provides:       tex(ot2-stix2text.pl) = %{tl_version}, tex(ot2-stix2textsc-bold.pl) = %{tl_version}
Provides:       tex(ot2-stix2textsc.pl) = %{tl_version}, tex(stix2-mathbb.pl) = %{tl_version}
Provides:       tex(stix2-mathbbit.pl) = %{tl_version}, tex(stix2-mathcal.pl) = %{tl_version}
Provides:       tex(stix2-mathex.pl) = %{tl_version}, tex(stix2-mathfrak-bold.pl) = %{tl_version}
Provides:       tex(stix2-mathfrak.pl) = %{tl_version}, tex(stix2-mathit-bold.pl) = %{tl_version}
Provides:       tex(stix2-mathit.pl) = %{tl_version}, tex(stix2-mathrm-bold.pl) = %{tl_version}
Provides:       tex(stix2-mathrm.pl) = %{tl_version}, tex(stix2-mathscr-bold.pl) = %{tl_version}
Provides:       tex(stix2-mathscr.pl) = %{tl_version}, tex(stix2-mathsf-bold.pl) = %{tl_version}
Provides:       tex(stix2-mathsf.pl) = %{tl_version}, tex(stix2-mathsfit-bold.pl) = %{tl_version}
Provides:       tex(stix2-mathsfit.pl) = %{tl_version}, tex(stix2-mathtt.pl) = %{tl_version}
Provides:       tex(t1-stix2text-bold.pl) = %{tl_version}
Provides:       tex(t1-stix2text-bolditalic.pl) = %{tl_version}
Provides:       tex(t1-stix2text-italic.pl) = %{tl_version}
Provides:       tex(t1-stix2text.pl) = %{tl_version}, tex(t1-stix2textsc-bold.pl) = %{tl_version}
Provides:       tex(t1-stix2textsc.pl) = %{tl_version}, tex(ts1-stix2text-bold.pl) = %{tl_version}
Provides:       tex(ts1-stix2text-bolditalic.pl) = %{tl_version}
Provides:       tex(ts1-stix2text-italic.pl) = %{tl_version}
Provides:       tex(ts1-stix2text.pl) = %{tl_version}, tex(ot1-stix2text-bold.tfm) = %{tl_version}
Provides:       tex(ot1-stix2text-bolditalic.tfm) = %{tl_version}
Provides:       tex(ot1-stix2text-italic.tfm) = %{tl_version}
Provides:       tex(ot1-stix2text.tfm) = %{tl_version}, tex(ot1-stix2textsc-bold.tfm) = %{tl_version}
Provides:       tex(ot1-stix2textsc.tfm) = %{tl_version}
Provides:       tex(ot2-stix2text-bold.tfm) = %{tl_version}
Provides:       tex(ot2-stix2text-bolditalic.tfm) = %{tl_version}
Provides:       tex(ot2-stix2text-italic.tfm) = %{tl_version}
Provides:       tex(ot2-stix2text.tfm) = %{tl_version}, tex(ot2-stix2textsc-bold.tfm) = %{tl_version}
Provides:       tex(ot2-stix2textsc.tfm) = %{tl_version}
Provides:       tex(stix2-mathbb.tfm) = %{tl_version}, tex(stix2-mathbbit.tfm) = %{tl_version}
Provides:       tex(stix2-mathcal.tfm) = %{tl_version}, tex(stix2-mathex.tfm) = %{tl_version}
Provides:       tex(stix2-mathfrak-bold.tfm) = %{tl_version}
Provides:       tex(stix2-mathfrak.tfm) = %{tl_version}, tex(stix2-mathit-bold.tfm) = %{tl_version}
Provides:       tex(stix2-mathit.tfm) = %{tl_version}, tex(stix2-mathrm-bold.tfm) = %{tl_version}
Provides:       tex(stix2-mathrm.tfm) = %{tl_version}, tex(stix2-mathscr-bold.tfm) = %{tl_version}
Provides:       tex(stix2-mathscr.tfm) = %{tl_version}, tex(stix2-mathsf-bold.tfm) = %{tl_version}
Provides:       tex(stix2-mathsf.tfm) = %{tl_version}, tex(stix2-mathsfit-bold.tfm) = %{tl_version}
Provides:       tex(stix2-mathsfit.tfm) = %{tl_version}, tex(stix2-mathtt.tfm) = %{tl_version}
Provides:       tex(t1-stix2text-bold.tfm) = %{tl_version}
Provides:       tex(t1-stix2text-bolditalic.tfm) = %{tl_version}
Provides:       tex(t1-stix2text-italic.tfm) = %{tl_version}
Provides:       tex(t1-stix2text.tfm) = %{tl_version}, tex(t1-stix2textsc-bold.tfm) = %{tl_version}
Provides:       tex(t1-stix2textsc.tfm) = %{tl_version}, tex(ts1-stix2text-bold.tfm) = %{tl_version}
Provides:       tex(ts1-stix2text-bolditalic.tfm) = %{tl_version}
Provides:       tex(ts1-stix2text-italic.tfm) = %{tl_version}
Provides:       tex(ts1-stix2text.tfm) = %{tl_version}, tex(STIX2Math.pfb) = %{tl_version}
Provides:       tex(STIX2Text-Bold.pfb) = %{tl_version}, tex(STIX2Text-BoldItalic.pfb) = %{tl_version}
Provides:       tex(STIX2Text-Italic.pfb) = %{tl_version}
Provides:       tex(STIX2Text-Regular.pfb) = %{tl_version}
Provides:       tex(ls1stix2.fd) = %{tl_version}, tex(ls1stix2bb.fd) = %{tl_version}
Provides:       tex(ls1stix2frak.fd) = %{tl_version}, tex(ls1stix2scr.fd) = %{tl_version}
Provides:       tex(ls1stix2sf.fd) = %{tl_version}, tex(ls2stix2.fd) = %{tl_version}
Provides:       tex(ls2stix2cal.fd) = %{tl_version}, tex(ls2stix2ex.fd) = %{tl_version}
Provides:       tex(ls2stix2tt.fd) = %{tl_version}, tex(ot1stix2.fd) = %{tl_version}
Provides:       tex(ot2stix2.fd) = %{tl_version}, tex(stix2.sty) = %{tl_version}
Provides:       tex(t1stix2.fd) = %{tl_version}, tex(ts1stix2.fd) = %{tl_version}

%description -n texlive-stix2-type1
The stix2 package provides minimal support for using the STIX
Two fonts with versions of TeX that are limited to TFM files,
Type 1 PostScript fonts, and 8-bit font encodings. Version
2.0.0 of the STIX fonts are being released in this format in
hopes of easing the transition from legacy TeX engines to
modern fully Unicode-compatible systems. The Type 1 versions
are merely a repackaging of the original OpenType versions and
should not be viewed as independent entities. Some glyphs that
are traditionally available in TeX math fonts are not yet
available in the STIX Two OpenType fonts. In such cases, we
have chosen to omit them from the stix2 package rather than
create incompatibilities between the OpenType and Type 1
versions. In addition, while development of the OpenType
versions is ongoing, no further updates are planned to the Type
1 versions of the fonts.

%package -n texlive-structmech
Summary:        A TikZ command set for structural mechanics drawings
Version:        svn47859
License:        GPLv3+
Requires:       texlive-base texlive-kpathsea

%description -n texlive-structmech
This package provides a collection of TikZ commands that allow
users to draw basic elements in material/structural mechanics.
It is thus possible to draw member forces, nodal
forces/displacements, various boundary conditions, internal
force distributions, etc.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD

cd %{buildroot}%{_texdir}/texmf-dist/
patch -p0 < %{_sourcedir}/texlive-bz#1442706-python-path.patch

install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="adobe/sourcecodepro adobe/sourcesanspro adobe/sourceserifpro \
public/skaknew"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tex/plain/standalone/standalone.*
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*


%files -n texlive-showtags
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/showtags/

%files -n texlive-showtags-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/showtags/

%files -n texlive-sort-by-letters
%license other-free.txt
%{_texdir}/texmf-dist/bibtex/bst/sort-by-letters/

%files -n texlive-sort-by-letters-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/bibtex/sort-by-letters/

%files -n texlive-splitbib
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/splitbib/

%files -n texlive-splitbib-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/splitbib/

%files -n texlive-stmaryrd
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/stmaryrd/
%{_texdir}/texmf-dist/fonts/map/dvips/stmaryrd/
%{_texdir}/texmf-dist/fonts/source/public/stmaryrd/
%{_texdir}/texmf-dist/fonts/tfm/public/stmaryrd/
%{_texdir}/texmf-dist/fonts/type1/public/stmaryrd/
%{_texdir}/texmf-dist/tex/latex/stmaryrd/

%files -n texlive-stmaryrd-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/stmaryrd/

%files -n texlive-skaknew
%license lppl1.txt
%{_datadir}/fonts/skaknew
%{_texdir}/texmf-dist/fonts/afm/public/skaknew/
%{_texdir}/texmf-dist/fonts/map/dvips/skaknew/
%{_texdir}/texmf-dist/fonts/opentype/public/skaknew/
%{_texdir}/texmf-dist/fonts/tfm/public/skaknew/
%{_texdir}/texmf-dist/fonts/type1/public/skaknew/

%files -n texlive-skaknew-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/skaknew/

%files -n texlive-skrapport
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/skrapport/

%files -n texlive-skrapport-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/skrapport/

%files -n texlive-slantsc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/slantsc/

%files -n texlive-slantsc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/slantsc/

%files -n texlive-shobhika
%license ofl.txt
%doc %{_texdir}/texmf-dist/doc/fonts/shobhika/
%{_texdir}/texmf-dist/fonts/opentype/public/shobhika/

%files -n texlive-simple-resume-cv
%license pd.txt
%doc %{_texdir}/texmf-dist/doc/xelatex/simple-resume-cv/
%{_texdir}/texmf-dist/tex/xelatex/simple-resume-cv/

%files -n texlive-simple-thesis-dissertation
%license pd.txt
%doc %{_texdir}/texmf-dist/doc/xelatex/simple-thesis-dissertation/
%{_texdir}/texmf-dist/tex/xelatex/simple-thesis-dissertation/

%files -n texlive-soup
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/soup/
%{_texdir}/texmf-dist/tex/latex/soup/

%files -n texlive-spark-otf
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/fonts/spark-otf/
%{_texdir}/texmf-dist/tex/latex/spark-otf/

%files -n texlive-spectralsequences
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/latex/spectralsequences/
%{_texdir}/texmf-dist/tex/latex/spectralsequences/

%files -n texlive-studenthandouts
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/studenthandouts/
%{_texdir}/texmf-dist/tex/latex/studenthandouts/

%files -n texlive-simplekv
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/generic/simplekv/
%{_texdir}/texmf-dist/tex/generic/simplekv/

%files -n texlive-short-math-guide
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/latex/short-math-guide/

%files -n texlive-simpleinvoice
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/simpleinvoice/
%doc %{_texdir}/texmf-dist/doc/latex/simpleinvoice/

%files -n texlive-spalign
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/spalign/
%doc %{_texdir}/texmf-dist/doc/latex/spalign/

%files -n texlive-stanli
%license lppl.txt gpl.txt
%{_texdir}/texmf-dist/tex/latex/stanli/
%doc %{_texdir}/texmf-dist/doc/latex/stanli/

%files -n texlive-statistics
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/statistics/
%doc %{_texdir}/texmf-dist/doc/latex/statistics/

%files -n texlive-statmath
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/statmath/
%doc %{_texdir}/texmf-dist/doc/latex/statmath/

%files -n texlive-stealcaps
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/stealcaps/
%doc %{_texdir}/texmf-dist/doc/latex/stealcaps/

%files -n texlive-stickstoo
%license ofl.txt lppl.txt
%{_texdir}/texmf-dist/fonts/afm/public/stickstoo/
%{_texdir}/texmf-dist/fonts/enc/dvips/stickstoo/
%{_texdir}/texmf-dist/fonts/map/dvips/stickstoo/
%{_texdir}/texmf-dist/fonts/tfm/public/stickstoo/
%{_texdir}/texmf-dist/fonts/type1/public/stickstoo/
%{_texdir}/texmf-dist/fonts/vf/public/stickstoo/
%{_texdir}/texmf-dist/tex/latex/stickstoo/
%doc %{_texdir}/texmf-dist/doc/fonts/stickstoo/

%files -n texlive-stix2-otf
%license ofl.txt
%{_texdir}/texmf-dist/fonts/opentype/public/stix2-otf/
%doc %{_texdir}/texmf-dist/doc/fonts/stix2-otf/

%files -n texlive-stix2-type1
%license ofl.txt lppl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/stix2/
%{_texdir}/texmf-dist/fonts/map/dvips/stix2/
%{_texdir}/texmf-dist/fonts/source/public/stix2/
%{_texdir}/texmf-dist/fonts/tfm/public/stix2/
%{_texdir}/texmf-dist/fonts/type1/public/stix2/
%{_texdir}/texmf-dist/tex/latex/stix2/
%doc %{_texdir}/texmf-dist/doc/latex/stix2/

%files -n texlive-structmech
%license gpl3.txt
%doc %{_texdir}/texmf-dist/doc/latex/structmech/

%files -n texlive-sourcesanspro
%license ofl.txt
%{_datadir}/fonts/sourcesanspro
%{_texdir}/texmf-dist/fonts/enc/dvips/sourcesanspro/
%{_texdir}/texmf-dist/fonts/map/dvips/sourcesanspro/
%{_texdir}/texmf-dist/fonts/opentype/adobe/sourcesanspro/
%{_texdir}/texmf-dist/fonts/tfm/adobe/sourcesanspro/
%{_texdir}/texmf-dist/fonts/type1/adobe/sourcesanspro/
%{_texdir}/texmf-dist/fonts/vf/adobe/sourcesanspro/
%{_texdir}/texmf-dist/tex/latex/sourcesanspro/

%files -n texlive-sourcesanspro-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/latex/sourcesanspro/

%files -n texlive-sourceserifpro
%license ofl.txt
%{_datadir}/fonts/sourceserifpro
%{_texdir}/texmf-dist/fonts/enc/dvips/sourceserifpro/
%{_texdir}/texmf-dist/fonts/map/dvips/sourceserifpro/
%{_texdir}/texmf-dist/fonts/opentype/adobe/sourceserifpro/
%{_texdir}/texmf-dist/fonts/tfm/adobe/sourceserifpro/
%{_texdir}/texmf-dist/fonts/type1/adobe/sourceserifpro/
%{_texdir}/texmf-dist/fonts/vf/adobe/sourceserifpro/
%{_texdir}/texmf-dist/tex/latex/sourceserifpro/

%files -n texlive-sourceserifpro-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/latex/sourceserifpro/

%files -n texlive-starfont
%license pd.txt
%{_texdir}/texmf-dist/fonts/afm/public/starfont/
%{_texdir}/texmf-dist/fonts/map/dvips/starfont/
%{_texdir}/texmf-dist/fonts/tfm/public/starfont/
%{_texdir}/texmf-dist/fonts/type1/public/starfont/
%{_texdir}/texmf-dist/tex/latex/starfont/

%files -n texlive-starfont-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/starfont/

%files -n texlive-sourcecodepro
%license ofl.txt
%{_datadir}/fonts/sourcecodepro
%{_texdir}/texmf-dist/fonts/enc/dvips/sourcecodepro/
%{_texdir}/texmf-dist/fonts/map/dvips/sourcecodepro/
%{_texdir}/texmf-dist/fonts/opentype/adobe/sourcecodepro/
%{_texdir}/texmf-dist/fonts/tfm/adobe/sourcecodepro/
%{_texdir}/texmf-dist/fonts/type1/adobe/sourcecodepro/
%{_texdir}/texmf-dist/fonts/vf/adobe/sourcecodepro/
%{_texdir}/texmf-dist/tex/latex/sourcecodepro/

%files -n texlive-sourcecodepro-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/latex/sourcecodepro/

%files -n texlive-staves
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/staves/
%{_texdir}/texmf-dist/fonts/tfm/public/staves/
%{_texdir}/texmf-dist/fonts/type1/public/staves/
%{_texdir}/texmf-dist/tex/latex/staves/

%files -n texlive-staves-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/staves/

%files -n texlive-stix
%{_texdir}/texmf-dist/fonts/enc/dvips/stix/
%{_texdir}/texmf-dist/fonts/map/dvips/stix/
%{_texdir}/texmf-dist/fonts/opentype/public/stix/
%{_texdir}/texmf-dist/fonts/tfm/public/stix/
%{_texdir}/texmf-dist/fonts/type1/public/stix/
%{_texdir}/texmf-dist/fonts/vf/public/stix/
%{_texdir}/texmf-dist/tex/latex/stix/

%files -n texlive-stix-doc
%{_texdir}/texmf-dist/doc/fonts/stix/

%files -n texlive-superiors
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/superiors/
%{_texdir}/texmf-dist/fonts/map/dvips/superiors/
%{_texdir}/texmf-dist/fonts/tfm/public/superiors/
%{_texdir}/texmf-dist/fonts/type1/public/superiors/
%{_texdir}/texmf-dist/tex/latex/superiors/

%files -n texlive-superiors-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/superiors/

%files -n texlive-stellenbosch
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/stellenbosch/
%{_texdir}/texmf-dist/tex/latex/stellenbosch/

%files -n texlive-stellenbosch-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/stellenbosch/

%files -n texlive-shuffle
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/shuffle/
%{_texdir}/texmf-dist/fonts/tfm/public/shuffle/
%{_texdir}/texmf-dist/tex/latex/shuffle/

%files -n texlive-shuffle-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/shuffle/

%files -n texlive-skmath
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/skmath/

%files -n texlive-skmath-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/skmath/

%files -n texlive-statex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/statex/

%files -n texlive-statex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/statex/

%files -n texlive-statex2
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/statex2/

%files -n texlive-statex2-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/statex2/

%files -n texlive-subsupscripts
%{_texdir}/texmf-dist/tex/latex/subsupscripts/

%files -n texlive-subsupscripts-doc
%{_texdir}/texmf-dist/doc/latex/subsupscripts/

%files -n texlive-susy
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/susy/

%files -n texlive-susy-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/susy/

%files -n texlive-shipunov
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/shipunov/
%{_texdir}/texmf-dist/scripts/shipunov/
%{_texdir}/texmf-dist/tex/latex/shipunov/

%files -n texlive-shipunov-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/shipunov/

%files -n texlive-shorttoc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/shorttoc/

%files -n texlive-shorttoc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/shorttoc/

%files -n texlive-show2e
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/show2e/

%files -n texlive-show2e-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/show2e/

%files -n texlive-showcharinbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/showcharinbox/

%files -n texlive-showcharinbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/showcharinbox/

%files -n texlive-showdim
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/showdim/

%files -n texlive-showdim-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/showdim/

%files -n texlive-showexpl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/showexpl/

%files -n texlive-showexpl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/showexpl/

%files -n texlive-spie
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bib/spie/
%{_texdir}/texmf-dist/bibtex/bst/spie/
%{_texdir}/texmf-dist/tex/latex/spie/

%files -n texlive-spie-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/spie/

%files -n texlive-sr-vorl
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sr-vorl/

%files -n texlive-sr-vorl-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sr-vorl/

%files -n texlive-suftesi
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/suftesi/

%files -n texlive-suftesi-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/suftesi/

%files -n texlive-sugconf
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sugconf/

%files -n texlive-sugconf-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sugconf/

%files -n texlive-svrsymbols-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/svrsymbols/

%files -n texlive-svrsymbols
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/svrsymbols/
%{_texdir}/texmf-dist/fonts/map/dvips/svrsymbols/
%{_texdir}/texmf-dist/fonts/tfm/public/svrsymbols/
%{_texdir}/texmf-dist/fonts/afm/public/svrsymbols/
%{_texdir}/texmf-dist/fonts/type1/public/svrsymbols/

%files -n texlive-swebib
%license lppl1.2.txt
%{_texdir}/texmf-dist/bibtex/bst/swebib/

%files -n texlive-swebib-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/swebib/

%files -n texlive-shade
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/shade/
%{_texdir}/texmf-dist/tex/generic/shade/

%files -n texlive-shade-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/shade/

%files -n texlive-systeme
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/systeme/

%files -n texlive-systeme-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/systeme/

%files -n texlive-shapepar
%{_texdir}/texmf-dist/tex/generic/shapepar/

%files -n texlive-shapepar-doc
%{_texdir}/texmf-dist/doc/generic/shapepar/

%files -n texlive-shdoc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/shdoc/

%files -n texlive-shdoc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/shdoc/

%files -n texlive-shadethm
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/shadethm/

%files -n texlive-shadethm-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/shadethm/

%files -n texlive-shadow
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/shadow/

%files -n texlive-shadow-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/shadow/

%files -n texlive-shadowtext
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/shadowtext/

%files -n texlive-shadowtext-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/shadowtext/

%files -n texlive-showlabels
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/showlabels/

%files -n texlive-showlabels-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/showlabels/

%files -n texlive-sidecap
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sidecap/

%files -n texlive-sidecap-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sidecap/

%files -n texlive-sidenotes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sidenotes/

%files -n texlive-sidenotes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sidenotes/

%files -n texlive-silence
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/silence/

%files -n texlive-silence-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/silence/

%files -n texlive-simplecd
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/simplecd/

%files -n texlive-simplecd-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/simplecd/

%files -n texlive-simplecv
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/simplecv/

%files -n texlive-simplecv-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/simplecv/

%files -n texlive-sides
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/sides/

%files -n texlive-sides-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/sides/

%files -n texlive-stage
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/stage/

%files -n texlive-stage-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/stage/

%files -n texlive-signchart-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/signchart/

%files -n texlive-signchart
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/signchart/

%files -n texlive-simpler-wick-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/simpler-wick/

%files -n texlive-simpler-wick
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/simpler-wick/

%files -n texlive-smartunits-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/smartunits/

%files -n texlive-smartunits
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/smartunits/

%files -n texlive-simplified-latex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/simplified-latex/

%files -n texlive-skak
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/skak/
%{_texdir}/texmf-dist/fonts/tfm/public/skak/
%{_texdir}/texmf-dist/tex/latex/skak/

%files -n texlive-skak-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/skak/

%files -n texlive-sudoku
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sudoku/

%files -n texlive-sudoku-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sudoku/

%files -n texlive-sudokubundle
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sudokubundle/

%files -n texlive-sudokubundle-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sudokubundle/

%files -n texlive-simurgh
%license gpl2.txt
%{_texdir}/texmf-dist/tex/lualatex/simurgh/

%files -n texlive-simurgh-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/lualatex/simurgh/

%files -n texlive-simplewick
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/simplewick/

%files -n texlive-simplewick-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/simplewick/

%files -n texlive-sitem
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sitem/

%files -n texlive-sitem-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sitem/

%files -n texlive-skb
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/skb/

%files -n texlive-skb-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/skb/

%files -n texlive-skdoc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/skdoc/

%files -n texlive-skdoc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/skdoc/

%files -n texlive-skeycommand
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/skeycommand/

%files -n texlive-skeycommand-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/skeycommand/

%files -n texlive-skeyval
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/skeyval/

%files -n texlive-skeyval-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/skeyval/

%files -n texlive-stex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/stex/

%files -n texlive-stex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/stex/

%files -n texlive-storebox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/storebox/

%files -n texlive-storebox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/storebox/

%files -n texlive-storecmd
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/storecmd/

%files -n texlive-storecmd-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/storecmd/

%files -n texlive-stringstrings
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/stringstrings/

%files -n texlive-stringstrings-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/stringstrings/

%files -n texlive-sttools
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sttools/

%files -n texlive-sttools-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sttools/

%files -n texlive-stubs
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/stubs/

%files -n texlive-stubs-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/stubs/

%files -n texlive-siunitx
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/siunitx/

%files -n texlive-siunitx-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/siunitx/

%files -n texlive-steinmetz
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/steinmetz/

%files -n texlive-steinmetz-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/steinmetz/

%files -n texlive-struktex
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/struktex/

%files -n texlive-struktex-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/struktex/

%files -n texlive-substances
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/substances/

%files -n texlive-substances-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/substances/

%files -n texlive-smalltableof
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/smalltableof/

%files -n texlive-smalltableof-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/smalltableof/

%files -n texlive-smartref
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/smartref/

%files -n texlive-smartref-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/smartref/

%files -n texlive-snapshot
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/snapshot/

%files -n texlive-snapshot-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/snapshot/

%files -n texlive-snotez
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/snotez/

%files -n texlive-snotez-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/snotez/

%files -n texlive-songbook
%license lgpl2.1.txt
%{_texdir}/texmf-dist/makeindex/songbook/
%{_texdir}/texmf-dist/tex/latex/songbook/

%files -n texlive-songbook-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/songbook/

%files -n texlive-songs
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/songs/

%files -n texlive-songs-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/songs/

%files -n texlive-smartdiagram
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/smartdiagram/

%files -n texlive-smartdiagram-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/smartdiagram/

%files -n texlive-soton
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/soton/

%files -n texlive-soton-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/soton/

%files -n texlive-soul
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/soul/

%files -n texlive-soul-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/soul/

%files -n texlive-spanish-mx
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/spanish-mx/

%files -n texlive-spanish-mx-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/spanish-mx/

%files -n texlive-sparklines
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sparklines/

%files -n texlive-sparklines-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sparklines/

%files -n texlive-spath3
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/spath3/

%files -n texlive-spath3-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/spath3/

%files -n texlive-sphack
%{_texdir}/texmf-dist/tex/latex/sphack/

%files -n texlive-sphack-doc
%{_texdir}/texmf-dist/doc/latex/sphack/

%files -n texlive-spot
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/spot/

%files -n texlive-spot-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/spot/

%files -n texlive-spotcolor
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/spotcolor/

%files -n texlive-spotcolor-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/spotcolor/

%files -n texlive-spreadtab
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/spreadtab/

%files -n texlive-spreadtab-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/spreadtab/

%files -n texlive-sphdthesis
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/sphdthesis/

%files -n texlive-sphdthesis-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/sphdthesis/

%files -n texlive-spverbatim
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/spverbatim/

%files -n texlive-spverbatim-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/spverbatim/

%files -n texlive-srbook-mem
%{_texdir}/texmf-dist/tex/latex/srbook-mem/

%files -n texlive-srbook-mem-doc
%{_texdir}/texmf-dist/doc/latex/srbook-mem/

%files -n texlive-srcltx
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/srcltx/

%files -n texlive-srcltx-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/srcltx/

%files -n texlive-sseq
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/sseq/

%files -n texlive-sseq-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/sseq/

%files -n texlive-sslides
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/sslides/

%files -n texlive-sslides-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/sslides/

%files -n texlive-stack
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/stack/

%files -n texlive-stackengine
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/stackengine/

%files -n texlive-stackengine-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/stackengine/

%files -n texlive-standalone
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/standalone/

%files -n texlive-standalone-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/standalone/

%files -n texlive-statistik
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/statistik/

%files -n texlive-statistik-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/statistik/

%files -n texlive-stdclsdv
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/stdclsdv/

%files -n texlive-stdclsdv-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/stdclsdv/

%files -n texlive-stdpage
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/stdpage/

%files -n texlive-stdpage-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/stdpage/

%files -n texlive-subdepth
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/subdepth/

%files -n texlive-subdepth-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/subdepth/

%files -n texlive-subeqn
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/subeqn/

%files -n texlive-subeqn-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/subeqn/

%files -n texlive-subeqnarray
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/subeqnarray/

%files -n texlive-subeqnarray-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/subeqnarray/

%files -n texlive-subfigmat
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/subfigmat/

%files -n texlive-subfigmat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/subfigmat/

%files -n texlive-subfigure
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/subfigure/

%files -n texlive-subfigure-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/subfigure/

%files -n texlive-subfiles
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/subfiles/

%files -n texlive-subfiles-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/subfiles/

%files -n texlive-substitutefont
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/substitutefont/

%files -n texlive-substitutefont-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/substitutefont/

%files -n texlive-substr
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/substr/

%files -n texlive-substr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/substr/

%files -n texlive-supertabular
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/supertabular/

%files -n texlive-supertabular-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/supertabular/

%files -n texlive-svg
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/svg/

%files -n texlive-svg-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/svg/

%files -n texlive-svgcolor
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/svgcolor/

%files -n texlive-svgcolor-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/svgcolor/

%files -n texlive-svn
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/svn/

%files -n texlive-svn-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/svn/

%files -n texlive-svninfo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/svninfo/

%files -n texlive-svninfo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/svninfo/

%files -n texlive-syntax
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/syntax/

%files -n texlive-syntax-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/syntax/

%files -n texlive-syntrace
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/syntrace/

%files -n texlive-syntrace-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/syntrace/

%files -n texlive-synttree
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/synttree/

%files -n texlive-synttree-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/synttree/

%files -n texlive-subfig
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/subfig/

%files -n texlive-subfig-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/subfig/

%files -n texlive-svg-inkscape-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/svg-inkscape/

%files -n texlive-swimgraf
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/swimgraf/

%files -n texlive-swimgraf-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/swimgraf/

%files -n texlive-syllogism
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/syllogism/

%files -n texlive-syllogism-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/syllogism/

%files -n texlive-sympytexpackage
%{_texdir}/texmf-dist/scripts/sympytexpackage/
%{_texdir}/texmf-dist/tex/latex/sympytexpackage/

%files -n texlive-sympytexpackage-doc
%{_texdir}/texmf-dist/doc/latex/sympytexpackage/

%files -n texlive-synproof
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/synproof/

%files -n texlive-synproof-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/synproof/

%files -n texlive-showhyphens
%{_texdir}/texmf-dist/tex/lualatex/showhyphens/

%files -n texlive-showhyphens-doc
%{_texdir}/texmf-dist/doc/lualatex/showhyphens/

%files -n texlive-spelling
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/spelling/
%{_texdir}/texmf-dist/tex/luatex/spelling/

%files -n texlive-spelling-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/luatex/spelling/

%files -n texlive-startex
%license pd.txt
%{_texdir}/texmf-dist/makeindex/startex/
%{_texdir}/texmf-dist/tex/startex/

%files -n texlive-startex-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/otherformats/startex/

%files -n texlive-svn-prov
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/svn-prov/

%files -n texlive-svn-prov-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/svn-prov/

%files -n texlive-shapes
%license lppl1.3.txt
%{_texdir}/texmf-dist/metapost/shapes/

%files -n texlive-shapes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/metapost/shapes/

%files -n texlive-slideshow
%{_texdir}/texmf-dist/metapost/slideshow/

%files -n texlive-slideshow-doc
%{_texdir}/texmf-dist/doc/metapost/slideshow/

%files -n texlive-splines
%license lppl1.3.txt
%{_texdir}/texmf-dist/metapost/splines/

%files -n texlive-splines-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/metapost/splines/

%files -n texlive-suanpan
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/suanpan/

%files -n texlive-suanpan-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/suanpan/

%files -n texlive-symbol
%license gpl.txt
%{_texdir}/texmf-dist/dvips/symbol/
%{_texdir}/texmf-dist/fonts/afm/adobe/symbol/
%{_texdir}/texmf-dist/fonts/afm/urw/symbol/
%{_texdir}/texmf-dist/fonts/map/dvips/symbol/
%{_texdir}/texmf-dist/fonts/tfm/adobe/symbol/
%{_texdir}/texmf-dist/fonts/tfm/monotype/symbol/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/symbol/
%{_texdir}/texmf-dist/fonts/type1/urw/symbol/
%{_texdir}/texmf-dist/tex/latex/symbol/

%files -n texlive-skull
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/skull/
%{_texdir}/texmf-dist/tex/latex/skull/

%files -n texlive-subfloat
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/subfloat/

%files -n texlive-subfloat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/subfloat/




%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
