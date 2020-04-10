<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<title>linear-regression-from-scratch</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000000;
  background-color: #ffffff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #ffffff;
  border: 1px solid #dddddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #cccccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #dddddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #dddddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #dddddd;
}
.table .table {
  background-color: #ffffff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #dddddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #dddddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #dddddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #ffffff;
  background-image: none;
  border: 1px solid #cccccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999999;
}
.form-control::-webkit-input-placeholder {
  color: #999999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333333;
  background-color: #ffffff;
  border-color: #cccccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #ffffff;
  border-color: #cccccc;
}
.btn-default .badge {
  color: #ffffff;
  background-color: #333333;
}
.btn-primary {
  color: #ffffff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #ffffff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #ffffff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #ffffff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #ffffff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #ffffff;
}
.btn-success {
  color: #ffffff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #ffffff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #ffffff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #ffffff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #ffffff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #ffffff;
}
.btn-info {
  color: #ffffff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #ffffff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #ffffff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #ffffff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #ffffff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #ffffff;
}
.btn-warning {
  color: #ffffff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #ffffff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #ffffff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #ffffff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #ffffff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #ffffff;
}
.btn-danger {
  color: #ffffff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #ffffff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #ffffff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #ffffff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #ffffff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #ffffff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #ffffff;
  border: 1px solid #cccccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #ffffff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #cccccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #dddddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #dddddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #ffffff;
  border: 1px solid #dddddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #dddddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #dddddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #ffffff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #ffffff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #dddddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #dddddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #ffffff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777777;
}
.navbar-default .navbar-nav > li > a {
  color: #777777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #cccccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #dddddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #dddddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #cccccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777777;
}
.navbar-default .navbar-link:hover {
  color: #333333;
}
.navbar-default .btn-link {
  color: #777777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #cccccc;
}
.navbar-inverse {
  background-color: #222222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #ffffff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #ffffff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #ffffff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #ffffff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #ffffff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #ffffff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #ffffff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #ffffff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #ffffff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #ffffff;
  border: 1px solid #dddddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #dddddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #ffffff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #ffffff;
  border-color: #dddddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #ffffff;
  border: 1px solid #dddddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #ffffff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #ffffff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #ffffff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #ffffff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #ffffff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #ffffff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #ffffff;
  border: 1px solid #dddddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #ffffff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #ffffff;
  border: 1px solid #dddddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #ffffff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #ffffff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #dddddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #dddddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #dddddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #dddddd;
}
.panel-default {
  border-color: #dddddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #dddddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #dddddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #dddddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #ffffff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #ffffff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000000;
  text-shadow: 0 1px 0 #ffffff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #ffffff;
  border: 1px solid #999999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #ffffff;
  text-align: center;
  background-color: #000000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #ffffff;
  background-clip: padding-box;
  border: 1px solid #cccccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #ffffff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #ffffff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #ffffff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #ffffff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #ffffff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #ffffff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #ffffff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #ffffff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #ffffff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eeeeee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #ffffff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #ffffff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #ffffff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
@media (max-width: 991px) {
  #ipython_notebook {
    margin-left: 10px;
  }
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#login_widget {
  float: right;
}
span#login_widget > .button,
#logout {
  color: #333333;
  background-color: #ffffff;
  border-color: #cccccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #ffffff;
  border-color: #cccccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #ffffff;
  background-color: #333333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  text-align: center;
  vertical-align: middle;
  display: inline;
  opacity: 0;
  z-index: 2;
  width: 12ex;
  margin-right: -12ex;
}
.alternate_upload .btn-upload {
  height: 22px;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #eeeeee;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #dddddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #dddddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #dddddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: baseline;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #eeeeee;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #dddddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #eeeeee;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #ffffff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #ffffff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #ffffff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI colors. */
.ansibold {
  font-weight: bold;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  border-left-width: 1px;
  padding-left: 5px;
  background: linear-gradient(to right, transparent -40px, transparent 1px, transparent 1px, transparent 100%);
}
div.cell.jupyter-soft-selected {
  border-left-color: #90caf9;
  border-left-color: #e3f2fd;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #e3f2fd;
  border-right-width: 1px;
  background: #e3f2fd;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected {
  border-color: #ababab;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #42a5f5 -40px, #42a5f5 5px, transparent 5px, transparent 100%);
}
@media print {
  div.cell.selected {
    border-color: transparent;
  }
}
div.cell.selected.jupyter-soft-selected {
  border-left-width: 0;
  padding-left: 6px;
  background: linear-gradient(to right, #42a5f5 -40px, #42a5f5 7px, #e3f2fd 7px, #e3f2fd 100%);
}
.edit_mode div.cell.selected {
  border-color: #66bb6a;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #66bb6a -40px, #66bb6a 5px, transparent 5px, transparent 100%);
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
    /* Old browsers */
    -webkit-box-flex: 0;
    -moz-box-flex: 0;
    box-flex: 0;
    /* Modern browsers */
    flex: none;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303f9f;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  padding: 0.4em;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. We need the 0 value because of how we size */
  /* .CodeMirror-lines */
  padding: 0;
  border: 0;
  border-radius: 0;
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000000;
}
.highlight-variable {
  color: #000000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000000;
  box-shadow: inset 0 0 1px #000000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #d84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
    /* Old browsers */
    -webkit-box-flex: 0;
    -moz-box-flex: 0;
    box-flex: 0;
    /* Modern browsers */
    flex: none;
  }
}
div.output_area pre {
  margin: 0;
  padding: 0;
  border: 0;
  vertical-align: baseline;
  color: #000000;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul {
  list-style: disc;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ul ul {
  list-style: square;
  margin: 0em 2em;
}
.rendered_html ul ul ul {
  list-style: circle;
  margin: 0em 2em;
}
.rendered_html ol {
  list-style: decimal;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
  margin: 0em 2em;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: #000000;
  background-color: #000000;
}
.rendered_html pre {
  margin: 1em 2em;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  background-color: #ffffff;
  color: #000000;
  font-size: 100%;
  padding: 0px;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: 1px solid #000000;
  border-collapse: collapse;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  border: 1px solid #000000;
  border-collapse: collapse;
  margin: 1em 2em;
}
.rendered_html td,
.rendered_html th {
  text-align: left;
  vertical-align: middle;
  padding: 4px;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #ffffff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #eeeeee;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #ffffff;
  background-image: none;
  border: 1px solid #cccccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget {
  float: right !important;
  float: right;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333333;
  background-color: #ffffff;
  border-color: #cccccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #ffffff;
  border-color: #cccccc;
}
.notification_widget .badge {
  color: #ffffff;
  background-color: #333333;
}
.notification_widget.warning {
  color: #ffffff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #ffffff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #ffffff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #ffffff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #ffffff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #ffffff;
}
.notification_widget.success {
  color: #ffffff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #ffffff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #ffffff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #ffffff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #ffffff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #ffffff;
}
.notification_widget.info {
  color: #ffffff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #ffffff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #ffffff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #ffffff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #ffffff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #ffffff;
}
.notification_widget.danger {
  color: #ffffff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #ffffff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #ffffff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #ffffff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #ffffff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #ffffff;
}
div#pager {
  background-color: #ffffff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  margin-top: 6px;
}
span.save_widget span.filename {
  height: 1em;
  line-height: 1em;
  padding: 3px;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  display: none;
}
.command-shortcut:before {
  content: "(command)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #eeeeee;
}
.terminal-app #header {
  background: #ffffff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Linear-Regression-with-One-Variable-from-Scratch">Linear Regression with One Variable from Scratch<a class="anchor-link" href="#Linear-Regression-with-One-Variable-from-Scratch">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Problem-Statement">Problem Statement<a class="anchor-link" href="#Problem-Statement">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Formulate a mathematical function f(x) which takes 'x' as input and predicts the correct value for 'y' according to the dataset given below. x and y are both floating point numbers.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Required-Libraries">Required Libraries<a class="anchor-link" href="#Required-Libraries">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># pandas for data processing</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>

<span class="c1"># numpy for mathematical calculations</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="c1"># matplotlib for visualization</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="DataSet">DataSet<a class="anchor-link" href="#DataSet">&#182;</a></h2><p><a href="https://www.kaggle.com/andonians/random-linear-regression/data">https://www.kaggle.com/andonians/random-linear-regression/data</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="1.1-Read-the-Data">1.1 Read the Data<a class="anchor-link" href="#1.1-Read-the-Data">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># path of the dataset</span>
<span class="n">path</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">&#39;../input/train.csv&#39;</span>

<span class="c1"># read the dataset</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Shape of the dataset = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>

<span class="c1"># lets see first 5 rows of the dataset</span>
<span class="n">data</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Shape of the dataset = (700, 2)
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt output_prompt">Out[2]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>24.0</td>
      <td>21.549452</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50.0</td>
      <td>47.464463</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15.0</td>
      <td>17.218656</td>
    </tr>
    <tr>
      <th>3</th>
      <td>38.0</td>
      <td>36.586398</td>
    </tr>
    <tr>
      <th>4</th>
      <td>87.0</td>
      <td>87.288984</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="1.2-Clean-the-data">1.2 Clean the data<a class="anchor-link" href="#1.2-Clean-the-data">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># drop any rows with &#39;nan&#39; values</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">dropna</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Shape of the dataset = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Shape of the dataset = (699, 2)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="1.3-Visualize-the-Data">1.3 Visualize the Data<a class="anchor-link" href="#1.3-Visualize-the-Data">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># let&#39;s visualize the dataset</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">500</span><span class="p">],</span> <span class="n">data</span><span class="o">.</span><span class="n">y</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">500</span><span class="p">],</span> <span class="s1">&#39;x&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s2">&quot;X vs Y&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s2">&quot;x&quot;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s2">&quot;y&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt output_prompt">Out[4]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>Text(0, 0.5, &#39;y&#39;)</pre>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="1.4-Break-into-Train-and-Cross-Valid-Set">1.4 Break into Train and Cross-Valid Set<a class="anchor-link" href="#1.4-Break-into-Train-and-Cross-Valid-Set">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># training dataset and labels</span>
<span class="n">train_dataset</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">500</span><span class="p">])</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">500</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<span class="n">train_labels</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">y</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">500</span><span class="p">])</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">500</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>

<span class="c1"># valid dataset and labels</span>
<span class="n">valid_dataset</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">x</span><span class="p">[</span><span class="mi">500</span><span class="p">:</span><span class="mi">700</span><span class="p">])</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">199</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>
<span class="n">valid_labels</span>  <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">y</span><span class="p">[</span><span class="mi">500</span><span class="p">:</span><span class="mi">700</span><span class="p">])</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">199</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span>

<span class="c1"># print the shapes</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Train Dataset Shape = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">train_dataset</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Train Labels  Shape = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">train_labels</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Valid Dataset Shape = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">valid_dataset</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Valid Labels  Shape = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">valid_labels</span><span class="o">.</span><span class="n">shape</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Train Dataset Shape = (500, 1)
Train Labels  Shape = (500, 1)
Valid Dataset Shape = (199, 1)
Valid Labels  Shape = (199, 1)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Forward-propagation">Forward propagation<a class="anchor-link" href="#Forward-propagation">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Equation for the function is:</p>
<p>f(x) = w*x + b</p>
<p>where <strong>w</strong> and <strong>b</strong> are the parameters we will learn through training.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">forward_propagation</span><span class="p">(</span><span class="n">train_dataset</span><span class="p">,</span> <span class="n">parameters</span><span class="p">):</span>
    <span class="n">w</span> <span class="o">=</span> <span class="n">parameters</span><span class="p">[</span><span class="s1">&#39;w&#39;</span><span class="p">]</span>
    <span class="n">b</span> <span class="o">=</span> <span class="n">parameters</span><span class="p">[</span><span class="s1">&#39;b&#39;</span><span class="p">]</span>
    <span class="n">predictions</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">multiply</span><span class="p">(</span><span class="n">w</span><span class="p">,</span> <span class="n">train_dataset</span><span class="p">)</span> <span class="o">+</span> <span class="n">b</span>
    <span class="k">return</span> <span class="n">predictions</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Define-Cost-Function">Define Cost Function<a class="anchor-link" href="#Define-Cost-Function">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Mean Squared Error</p>
<p>cost = [(y - f(x)) ^ 2] * 0.5</p>
<p>where <strong>y</strong> are the actual or true labels and <strong>f(x)</strong> are the predicted values.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">cost_function</span><span class="p">(</span><span class="n">predictions</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">):</span>
    <span class="n">cost</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">((</span><span class="n">train_labels</span> <span class="o">-</span> <span class="n">predictions</span><span class="p">)</span> <span class="o">**</span> <span class="mi">2</span><span class="p">)</span> <span class="o">*</span> <span class="mf">0.5</span>
    <span class="k">return</span> <span class="n">cost</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Gradient-Descent-for-Backpropagation">Gradient Descent for Backpropagation<a class="anchor-link" href="#Gradient-Descent-for-Backpropagation">&#182;</a></h2><p>Using Chain Rule:</p>
<p>c = cost <br>
f = f(x)</p>
<ul>
<li>Partial Derivative of <strong>cost function</strong> w.r.t <strong>w</strong> <br>
dc/dw = dc/df * df/dw <br></li>
<li>Partial Derivative of <strong>cost function</strong> w.r.t <strong>b</strong><br>
dc/db = dc/df * df/db <br></li>
</ul>
<p>Partial Derivatives:</p>
<ul>
<li>dc/df = (y - f) * -1</li>
<li>df/dw = x</li>
<li>df/db = 1</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">backward_propagation</span><span class="p">(</span><span class="n">train_dataset</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">,</span> <span class="n">predictions</span><span class="p">):</span>
    <span class="n">derivatives</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
    <span class="n">df</span> <span class="o">=</span> <span class="p">(</span><span class="n">train_labels</span> <span class="o">-</span> <span class="n">predictions</span><span class="p">)</span> <span class="o">*</span> <span class="o">-</span><span class="mi">1</span>
    <span class="n">dw</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">multiply</span><span class="p">(</span><span class="n">train_dataset</span><span class="p">,</span> <span class="n">df</span><span class="p">))</span>
    <span class="n">db</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
    <span class="n">derivatives</span><span class="p">[</span><span class="s1">&#39;dw&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">dw</span>
    <span class="n">derivatives</span><span class="p">[</span><span class="s1">&#39;db&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">db</span>
    <span class="k">return</span> <span class="n">derivatives</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Update-the-Parameters">Update the Parameters<a class="anchor-link" href="#Update-the-Parameters">&#182;</a></h2><ul>
<li>w = w - (learning_rate * dw)</li>
<li>b = b - (learning_rate * db)</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">update_parameters</span><span class="p">(</span><span class="n">parameters</span><span class="p">,</span> <span class="n">derivatives</span><span class="p">,</span> <span class="n">learning_rate</span><span class="p">):</span>
    <span class="n">parameters</span><span class="p">[</span><span class="s1">&#39;w&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">parameters</span><span class="p">[</span><span class="s1">&#39;w&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">learning_rate</span> <span class="o">*</span> <span class="n">derivatives</span><span class="p">[</span><span class="s1">&#39;dw&#39;</span><span class="p">]</span>
    <span class="n">parameters</span><span class="p">[</span><span class="s1">&#39;b&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">parameters</span><span class="p">[</span><span class="s1">&#39;b&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">learning_rate</span> <span class="o">*</span> <span class="n">derivatives</span><span class="p">[</span><span class="s1">&#39;db&#39;</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">parameters</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Train-the-Data">Train the Data<a class="anchor-link" href="#Train-the-Data">&#182;</a></h2><p>Sequence of Steps:</p>
<ol>
<li>Forward Propagtaion</li>
<li>Cost Function</li>
<li>Backward Propagation</li>
<li>Update Parameters</li>
</ol>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">train</span><span class="p">(</span><span class="n">train_dataset</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">,</span> <span class="n">learning_rate</span><span class="p">,</span> <span class="n">iters</span> <span class="o">=</span> <span class="mi">10</span><span class="p">):</span>
    <span class="c1">#random parameters</span>
    <span class="n">parameters</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>
    <span class="n">parameters</span><span class="p">[</span><span class="s2">&quot;w&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span> <span class="o">*</span> <span class="o">-</span><span class="mi">1</span>
    <span class="n">parameters</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">)</span> <span class="o">*</span> <span class="o">-</span><span class="mi">1</span>
    
    <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">()</span>
    
    <span class="c1">#loss</span>
    <span class="n">loss</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span>
    
    <span class="c1">#iterate</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">iters</span><span class="p">):</span>
        
        <span class="c1">#forward propagation</span>
        <span class="n">predictions</span> <span class="o">=</span> <span class="n">forward_propagation</span><span class="p">(</span><span class="n">train_dataset</span><span class="p">,</span> <span class="n">parameters</span><span class="p">)</span>
        
        <span class="c1">#cost function</span>
        <span class="n">cost</span> <span class="o">=</span> <span class="n">cost_function</span><span class="p">(</span><span class="n">predictions</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">)</span>
        
        <span class="c1">#append loss and print</span>
        <span class="n">loss</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">cost</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Iteration = </span><span class="si">{}</span><span class="s2">, Loss = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">,</span> <span class="n">cost</span><span class="p">))</span>
        
        <span class="c1">#plot function</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">train_dataset</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">,</span> <span class="s1">&#39;x&#39;</span><span class="p">)</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">train_dataset</span><span class="p">,</span> <span class="n">predictions</span><span class="p">,</span> <span class="s1">&#39;o&#39;</span><span class="p">)</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
        
        <span class="c1">#back propagation</span>
        <span class="n">derivatives</span> <span class="o">=</span> <span class="n">backward_propagation</span><span class="p">(</span><span class="n">train_dataset</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">,</span> <span class="n">predictions</span><span class="p">)</span>
        
        <span class="c1">#update parameters</span>
        <span class="n">parameters</span> <span class="o">=</span> <span class="n">update_parameters</span><span class="p">(</span><span class="n">parameters</span><span class="p">,</span> <span class="n">derivatives</span><span class="p">,</span> <span class="n">learning_rate</span><span class="p">)</span>
        
    <span class="k">return</span> <span class="n">parameters</span><span class="p">,</span> <span class="n">loss</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Training">Training<a class="anchor-link" href="#Training">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">parameters</span><span class="p">,</span><span class="n">loss</span> <span class="o">=</span> <span class="n">train</span><span class="p">(</span><span class="n">train_dataset</span><span class="p">,</span> <span class="n">train_labels</span><span class="p">,</span> <span class="mf">0.0001</span><span class="p">,</span> <span class="mi">20</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 1, Loss = 5868.852923980964
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 2, Loss = 2664.843407075815
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 3, Loss = 1211.1807402567006
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 4, Loss = 551.6523780779357
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 5, Loss = 252.42362953038878
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 6, Loss = 116.663214770032
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 7, Loss = 55.06856411319252
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 8, Loss = 27.12300277918117
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 9, Loss = 14.444070542060496
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 10, Loss = 8.691624836152005
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 11, Loss = 6.081733741521813
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 12, Loss = 4.897623154856925
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXoAAAD8CAYAAAB5Pm/hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4wLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvqOYd8AAAIABJREFUeJzs3Xtc1NeZ+PHPmRs3BRGIOogSQCXRYIlGDGq0mktTc7Pb5qKSaOIltll3m243Tdxus7vVNPtL011/6c9bEk1Rm7Zpyc3amGA0KgkqoRJN0ABeuKgBRETuzJzfHzPzZUDUUUFheN6vF2Hmy3eY72SSZw7Pec5zlNYaIYQQ/st0rS9ACCFE15JAL4QQfk4CvRBC+DkJ9EII4eck0AshhJ+TQC+EEH5OAr0QQvg5CfRCCOHnJNALIYSfs1zrCwCIjIzUsbGx1/oyhBCiR8nJyanQWkdd7LxuEehjY2PZu3fvtb4MIYToUZRSR305T1I3Qgjh5yTQCyGEn5NAL4QQfk4CvRBC+DkJ9EII4eck0AshxFW2cnshWYUVbY5lFVawcnthlzyfBHohhLjKkgaH8dTGXCPYZxVW8NTGXJIGh3XJ80mgF0KITuTLaD01PpJXZibz1MZcXt5ykKc25vLKzGRS4yO75Jok0AshRCfydbSeGh/J7JQhLN9awOyUIV0W5MGHQK+Uel0p9Y1Sar/Xsf5KqQ+VUl+7v4e7jyul1HKlVIFSKk8pdXOXXbkQQnRD5xut55VUtxnpZxVWsDbrCBPiI1iffeycvwI6ky8j+nXAd9od+xmQqbUeBmS67wPcDQxzfy0AVnTOZQohRM/R0Wj9aGUtC9NzyCqs4P7f7mTO67tpcTgZEhHMKzOTeWLdHu7/7c4uuZ6LBnqt9SfAqXaH7wfecN9+A3jA6/jvtMtnQD+l1KDOulghhOgJsgorWJ99jMVTE4zR+raD5TQ0OViYnkN1XTNNDk1ji5NtB8s5UFZNQ7OTiBBbl1zP5TY1G6C1Pg6gtT6ulLrOfTwaKPY6r8R97PjlX6IQQvQcnpy8Z3J1fHwET23MJTzYSrNT42hsoaahBQCnhjP1TSzblM/MlBhi+od0yTV19mSs6uCY7vBEpRYopfYqpfaWl5d38mUIIcS1sfqTIhZNiSM1PtKotFk0JY4+gRasJoWzXUSsbXIyfGAfNu8/2e3KK096UjLu79+4j5cAMV7nDQbKOvoFWuvVWuuxWuuxUVEXbacshBA9woLb4lixrYiswgqSBoexMD2H5ZkF3JM0CNXBUDgixMrBE2e5e9SALqu8udzUzbvAY8Cv3N/f8Tr+lFLqTSAFqPakeIQQojfwrrq5YWBfWhxOLGYTb+eW0eRoHc7vsv0QuzoNLUAglOX2Y03kVuZPiu/0a7pooFdK/R6YAkQqpUqAX+AK8H9USj0BHAN+4D79r8B3gQKgDpjb6VcshBDd2MrthSQNDjOqbgKtJkYPDmNnQSX7bY8RopqNc71H+HbTae7LvB0mHe70a7pooNdaP3KeH03r4FwN/OhKL0oIIbobTwD35N49+fS8kmqenBxPVmEFeSXVRroGYEJ8BNmHK9sE+Y7SN+Ca4LzunALHztEtthIUQoju7mhlLb/9uIBVaWM4WlnL8syv0VozfGBfzCaMPHzS4DBaHE4c2jVi325xp2jgvEG+q0kLBCFEr+dLf5p7R9sBWJieQ0Ozk7omB/XNTvoGWFi2KZ8Wh5N7R9t5b18ZFrOJ6TcN5MVjD2E3nUYp34J8V30OyIheCNEreadiPKP1xdMScDhpk34pPlXL0hlJpMZHsiptDLNfzSYjtxSLCUxKsbOgEptZoZTila0F5B47zdagZxj41REw+R68NaD6dM36Ugn0QoheydN87JWZydw72s47fy9j6aZ8ZiRH89uPCwAYFxvOhmzXGtCY/iF8sP+4UQff4gSTct9RiqYWB1mFlXwS/DMGNh7zaQSvcX0QaOAE4RyesZPUTn+lEuiFEL2Udxnk7JQhmE0Km8VERm4pgVYTr8+5hdT4SJZk5LEhu5gAs6LRoTEpGNI/mCOVdTg1hAVaeLplNbOsWzErJzgunqbR7givzEHw8xMo4LB7MrcrauklRy+E6LW8m4/dfsN1mDoI0EtnJGEPC6TRXQMfaDW3+fnTLat51PwRFuVE4VuQP6n6M8b8FlkzjabApMZH8uTkzq+hBwn0QohezNN8bEaynYzcMkxKsXhqAlazyeg0uSQjj7LqBvoGuhIgjc0OjlTWsd/2GIcDZvKo+SOf0zQaOK7D+d+kd4y/JrqyPbGHpG6EEL2G9wSsp/nYoilxvL7zCAEWE2aTovxsI4unJfDylkM8sW4P9c1OpiVGccv1Efxg2x30d1Yav8/Xckmt4bAphnscL2E2KVaNthupo65K13hTrjVO19bYsWP13r17r/VlCCH83LN/yeP9vOOsShvD6k+KiO4XyLv7jnNd3wC+qWnkvtGD2F92hqLyWhxOTVOLE601wQEWsqw/ok9T+SXXwmvgoHMw32n67za5/86glMrRWo+92HmSuhFC+IXz1cLPWbu7zfEWh5N5b+ylvKaRjdnFNLU4GXd9fxZPS2BjdjFxkX0AMJsU9462s8f6BHn6Qfo0X2KQH/sEPF/Np2mFPKBf6oyXeNkk0Ash/ML59mqdkBBhHPcseqprcnCg7AwmBY0tThqaHazYVsSEhAgyckuZmxrL3NRYfn7gO4Sb6l0Lnny4Bg2gzK4gf8/LZBVWsDA9B6vZdE7u/2qSHL0Qwi+0L5dcn33M2PxjpD3MOO7NoWGUPZSM3DImJkSwq6CSkfZQxmc9zq3sv+QFTw4ViOUXJ41j7+1zdWlflTbG2IRkYXoO7+0r6/K8vDcZ0Qsh/EZHe7W2P97s0FjNreF7f9kZQgMt7CyoxGpWrHT+J7ey31UqeZHn017fa7Hy85s+bPPzoREhRpD3XMeqtDEMjeianaTOR0b0Qgi/MGftbqL7BbJ5/0ljr9bK2kZKTzew4LY41mcfIzbCtdDJZlaMtIdyoOwMAGcaWvib7aeMUKVw2vcA3xg4gHW3bubJyfHkFVYwtKS6zXkd1cWnxkde1dE8yIheCOEnovsFsiG7mLtHDeDpO0dw96gBbMgupuRUHQvTc3hlZjK3xkdgMyuaHJqyqnrjsZvdQd6XXLwG6k19+TStkNTm33K0spaswoo2C57aN0S71iTQCyH8Qkz/EGalxLAxu5gHV2axMbuYWSkxhAS2Ji6GRoTw0++MwGpWVNU387ltHocDZpJoKvVpRasGThPMyvGZbfrkdDQJ3FX7v14OSd0IIbqN823usfqTIhbcFgecu9GHd3pkepKdr0+eZfeRKmLCg5ieZCemfwhJg8N4Yt0erusbyKm6JgKtZvZa5xKq63xb1apht0pikfnfmTw8koytBSyemmCkYM43CdxdSKAXQnQb3h0lvVsFL56WYNxelTbGGDW/MjPZeOzRylpe3nKQZocmJjyI4qp6Zr+azUO3xGA2QX2zk6OnXK0LQkyu7fwuOop3/2OHcyQH71zHImDZpnxmJNtZn32M8fERRs7dM9nr/QHQXUigF0J0G+1LJD1q6luM27/dWkBeaTWr0saQ5zX5mX/8DE0ObfSJV4BTw7u5pazgvzgccMDoCexTTbyGQhXDHY0v8tz0RKNE87npiTic8IOxMW0+bNZnHzMmgT0fAN2FBHohRLfSfnQMnHPbUx7pGfW3OJz0C7YxLTGKzPxyjp6qAyAs0Mz/dfwnk0wHWkfvPoziFXBYxXB7w4uMiw1n/qR4Vm4vPCcl88rMZN7bV8YHB04aPxsfH2F8AHSXYC+9boQQ3YonLTM7ZQhrs44AMDc11rg9pH8wB8rOEGQ1MX9SHGt2FFHf7GRA3wDONDS7etQ4NJ/bniBcuSprfG4+BqiAMJYkvs+G7GJGDOzDoRNneW56IvMnddxC2Htewfs1tJ8/6Aq+9rqREb0Qotton3v3BPe+Qa2h6oFkO0XlZ6lvdrJ8awE2iwmrWXGyphGAIKuJXOsT9NP1lxTgwVVR849Rf2Knu2Jn6Ywk1uwoZNmmfIAOg313qZW/EBnRCyG6DV+rbswmWOoOvuAK7qGBVjIbHyZENbt2b/LxObWGZhXA3rQveXzdHhqanUxMiGT9vBTjnDU7CtlVUMm6ueM67bV2Bl9H9BLohRA9yq0vZFJR04gyKZpanACYFeyzPkaIava5XNLzSdBIAE8OfZ8Ft8WxMD2Hm6LDyD9R061y7OcjbYqFEN3K+doIX+oK0hCbmWanxul0MrR/MP9peZ2DttmEmC4e5D27PJWEj2PVtz93rW41bzA6XK5KG8PG+eOv6u5PV4MEeiHEVXG0srZNi15PC9+jlbXGOb58GNxyfX8sJmhxwo/qVpDmtV/rhWgNNYTwaVohMf/8IU9OjjfKOXcVVLYZwXvv/uQPZDJWCHFV3Dvazvt5x1mYntOmisbTIx7aLpjy3u7vrpEDjH4yQyNC+DL4SawtZ1w18b4segJOq2D+O+lvvNAuHXO+idPuNqF6JSTQCyGuCk+L3sfX7XFVy5gV6x4f12bUvPqTIhZNaZsrXzQljqLyWlT6A2i+4Elaa919qYn39Ij/qoPukr3FFQV6pdSPgXm4/n1+AcwFBgFvAv2Bz4E0rXXTFV6nEKKH8K6cmbN2NxMSIhhpDyOvpJqkwWG0OFxj7CaH5kBZdZtWB7fEhvObD7+mxeEkq7CSGcnRLM8s4M8hLzKML/BxzZPBoQJ5dUoWT+JfI/RLddk5eqVUNLAYGKu1HgWYgYeBF4HfaK2HAVXAE51xoUKI7ss7t+5Jv6zZUYhJucog572xF7MJ5q7dQ4tTMzEhgiCriWWb8vnT3mLj94QF2ahrctDk0IyLDce57w/8Tf+QYbU5l7TT0/Fhs+D5aiy/ONnli5Z6giudjLUAQUopCxAMHAemAm+5f/4G8MAVPocQopvz3q81NT6SRVPiWLYpn7AgG8E2M3VNDlZvL6KxxcmslBjWzxvPa3NuwWJWZOSWGXu0ZuSWGgugBh57jxesrxKtKnwO8igzJ4bN4p3BP+nKl9vjXHbqRmtdqpR6CTgG1ANbgBzgtNba04GoBIi+4qsUQnRreSXVLJoS16ZVr2ej7cVTE/isqNLdOjiQpTOSWLm9ELMJLCaFPSyItVlHXP1qgqxscizArqoA31sXABAQBs8eYxDwZJe8yp7rsgO9UiocuB+4HjgN/Am4u4NTO1yRpZRaACwAGDJkSEenCCF6CM+IfvLwSJZvLTA22p6RHM2rOw9T1+Qgqo+N4qoGlmTkcby6ga355djMivjrQvimsIH6ZifbzD/kOlXl26In93cFRpAXHbuS1M3twGGtdbnWuhn4C5AK9HOncgAGA2UdPVhrvVprPVZrPTYqKuoKLkMIca150jVv55aROKAPOwsqmZkSw432vtQ1OQi2mVkwOY4Ai4kN2cV86d6rtcmhOXmmkVfVLzkcMJPrOOVzkP+Mm/g0rRCer5YgfxFXEuiPAeOVUsFKKQVMA74EPga+7z7nMeCdK7tEIUR39+xf8lieWcADydHknzzLxIRI3t13nOWZBcxKieHVx8bicMLaubdgNilOnGk0cvHPlD9Dqtrv036t9djYNOw/GWN+C532dq+torlUlx3otdbZuCZdP8dVWmkCVgPPAE8rpQqACOC1TrhOIUQ39uXxMzQ2O/joq5MsnprAvpLTNDY7sJoV7+47Dri6PB4oq8bhdCVd3jX9hEOWR9r2ir+QsBi2Dvs3fvRFArNThkiQvwRXVEevtf4F8It2h4uA7tXiTQjRpe5JGkRecTVmk6vJWIvDSbNDM7R/MPknaliYnsPtNwwgI7cUgA8D/5UEffENucGVpmkMHMDn923j5xtzWTx1SLfcxak7k143QojL4l07//vsYqYmRuHQrh2gHBqmJkZxoroRi9lEfVMLGbmlbLb9lMMBM0mgxOeKmsbAAfzH8LeM1ghP3znC75qOdTUJ9EKINnztMuldO68UZOaXG22Dm1qcZOaXExxg5lP1OF9bZ3I4YCaJqtSnXLwGjvUbB89XE/izQwyNCPHrpmNdTQK9EKINX7pMQtuNvIOsZuN4RIjVuP3nmpmEOM+6grvyrS5eAzscI/lgzErjmKfTZPvnl1WvvpFAL4Row9NNcmF6DjPXfMa8N/a2Oe49uvds5L2/7AwmdxCvrG1ml+2HHA6YSZiu9X07Pw2l1qGMMb/FwTvTcTg793X1ZhLohRDMWbubNTtag/eqtDHUN7WQVVhJXZODxdMS2rQNThocxsrthazZUehaBRsfgcUd6XfZfohdnfZ5BO9RZhvKhJoXmJ0yhPmT4mW03omkTbEQApOizQbYm/LKcKfbsVlMLM8s4OP8cr4orWZV2hhS4yM5UFbNsk35fDsxilvjI1hbfBdWd0S5pNYFkYlk3b2Jp6SipstIoBdCMCA0EKtZsWxTPm/llHDwxFkARtr7cuxUPY0trrbBgdbWJMD7ecexmhV7jlSx8sgdWC9xBA+0CfKeydbx8RFt7osrJ6kbIfyQd+WM57Z3br19Fc29o+0EWM0ohRHkg21mlky/kcXTEmhqcTKgbwAmpViYnsPLWw5SVF7LNvMPyeNBrD7u9KSBJkuoq23B89XwVDZ5JdVSUdPFJNAL4Ye8Sx89G3ssTM8haXCYkWc/WllrfBikxkdy3+hBOL1aEM5Idk2+rthWxKyUGEwmhdaaxhYny7cW8BFPMkhVofAtyKs+g/g0rZDx+vU25ZtSUdP1lNYdNpe8qsaOHav37t17rS9DCL/iCeizU4YY+7MmRYeR586zAzy1MZdFU+J4c3cxheW15/yO+KgQHh4Xw4ptri3+bvvwPoarElchvK/7tWo4ocI5nLbXmNDNK6mWQN4JlFI5WuuxFztPcvRC+ClP6ePyrQUsnpoAuFatevLs3huEhAS46uADLCYGhgVSUlWHwwmnapsIzXyWPXyIKdMJ3nl4X0bxmMh69GsWpudwz74yYzs/yb1fXZK6EcJPZRVWsD77GIunJrA26whrs46weGoCVrPJyLOv2FbEA8l2zjY6sJgUNouJmPAgHE5XJc4/N63iQT7AjNOnFA205uI1Cp6vMso1h0aEdPErFucjgV4IP+RJ27wyM5nx8RHG8e1fl3Pf6EE0O1x59snDo/jgwEn6BVkJspm5/Ybr2FlQycHANAptM3nU8pHv2/jhCvA11ig+TStkrPlPbeYAJFVz7UigF8IPeVey5JW4cvKr0sYQEWJjQ3YxWsNIeygZuaXUNTn40dR4Fk9L4O3cMvIDZ2PTDp960oBrRat2fz9BOPsf/kwqZ7oZydEL4Ye8R8/tR9KfFZ2irsnBmfpmwFVGCfD9zInMC6wDfK+H1xpOBMQy6Ll9Rk8cycV3PzKiF6IH87XTpEdeSTWvPjaWcbHhFFfVMy42nFcfG8tDmZPoR50rD3+R59Re379Wgzn8UCaA5OK7MQn0QvRg3vXyQJteNB3x7PK050gV42LDuafk14xPH0Zfan0K8E5lRo19Ap6vRj1fTUXa9jbpGcnFd0+SuhGiB1i5vZCkwWFtUiFZhRWs/sRV3+6pl1+ffYxFU+LIK6nuMG2yZkchyzbl89z0ROZX/xZ9wrfJVg0oZUX9ou1fD5Ke6Rkk0AvRTXkHd8/IfdGUOBzO1pH8t2LCWJ5ZwO03DGD51gJmJEezPLOAe5IGdfg7dxVUcjBwLrbMRsCHNI2rGJ5Gp4n0O7KZD7LgqQeS1I0Q3ZR3WsZ7cdPBE2eM0sl5k+JwODUZuaWMiw0nI7cUh1MbvePbW1dyHzYafXp+DdSqPsQ1bORHcR+wq6Dyoqkh0T3JiF6Ibsp7B6cbBvYlr7SaB5LtZOSWGStd39tXhtm90Gn3kSpsFhNmU9tx+srthdxf8msGFbwJ2nHR5/W0LWgw96XPv5fwnDvd80CyXbpK9lAyoheiG/O0MdhVWElji5OPvvrGWOm6MD0HgMXTEozdnUzKdT+vpBrefxr+oz8LP76ZgV9v8DnI77d/n1dv/5wJai1ZhRXMnxRvfMDMThkiQb4HkhG9EN2Yp43BjORoMnJLjV2cPOKiQlieWYDVbOLmIeH8vfg0yzML2DLsHfh6A+DjoidAKzOmMXO46Z6XuQkYaQ8zKmq2H6pg8dQE2RSkh5JAL0Q35d3GIK+kmiXTE/n1lkNGk7Lx8RG8+DfXrlCebpSk38+tej987fvzaA2NKoDAX3zT5rgnmMumID2fpG6E6Ka82xg8OTmekfYwrGYTqfERrM8+BsDdowYZW/ul7nycW9l/aa0LNNQqK5+nfQmcu9hKNgXxDxLohbjGzre6FVpH1Z7R/aq0Mdw2PMqonU8aHEbqzsfRz4ehD2/3uQGZ1vA7x+1c37iRF0ZvPWfjbw/ZFMQ/SOpGiGtgztrdTEiIYP6keKOM8u5RA9j8xQnuvmkgm/ef5JWZyYBrkdPvs4vbjKw9NfWD33sEfXq37wEecGBio3Mqv2h5HItJsTG7mLomB9sPVUhKxk9JoBfiGpiQEMGyTa78usMJyTFhbMguJjYimA3ZxUxLjGL1J0VsyitjY3Yx306MAloXK705/hh9Mp9kEBU+tS5wYKJ82CM8eXom+cdrsFlMLJ4Uy9qsI9Q2thglmxLk/ZMEeiGugfmTXKmPZZvyGT6wDwdPnGVUdCj7S88wKjqUzPxyYsID2XawnFkpMUxPshvllH+eUEL8Z0swU3/R59HAflsyNQ+9xVMbcxnaHxpbnPzLXcOZPymeytpG4wNGKmr81xUFeqVUP+BVYBSu/6YeBw4CfwBigSPAg1rrqiu6SiH8QPt+NfMnxfPnvSXknzhLTHggB0rPMC42nD1HqogJD6S4qoGoPlY27z9JREgAW1jIQF0Fu3zvMPkZN6EfesuYRF39SRFLpieyYlsRX5ad4e3cMmalxBDTP8RIIUn6xv9c6Yj+f4G/aa2/r5SyAcHAc0Cm1vpXSqmfAT8DnrnC5xGix/MOpHkl1ew5XEn+ybNGUI+NCGb3kSpG2UPZX3aGqD5Wys82ExsRzEM772Sg6bTPW/kdDb2F79U+c07FjOd2TX2LuzeOnaUzkozHeq5NAr1/uexAr5QKBW4D5gBorZuAJqXU/cAU92lvANuQQC96Ee+Ru2fS1bP46JWZycx7Yy8mBWcbHUxLjOKW6yP4YP9xcourGRAawP6yM8bx72y7n6Fni8Hk2yhe4QryU775MYundryK1Xsv2fXZx4xeOiDdKP3VlYzo44ByYK1SajSQA/wTMEBrfRxAa31cKXVdRw9WSi0AFgAMGTLkCi5DiGvvfJ0mTcqVhw+0mnhtzi0cKKumrsnVimBUdCi5xdWcONPIl+7gnnvsNJ+GPsfAI0dciU983O3JGkRmwhIO27/Lim1FLJ7qalncN8iCw9m6y5T3IixZANV7XEkdvQW4GVihtU4GanGlaXyitV6ttR6rtR4bFRV1BZchxLV3vk6TB0rPYDZBQ7OT//nwEEs35WM1K/oFWzlaWcfk4ZEcKDuD1awYHx/BloBnGNh0xNjpyadcfFgM3Lucw/bvsmxTPoumxPH0nSOMazB7/V8uC6B6J6W1vvhZHT1QqYHAZ1rrWPf9SbgCfQIwxT2aHwRs01qPuNDvGjt2rN67d+9lXYcQ3YVntOzpNHn7DdeRkVsGQFQfG+Vnm1C4gvO3YsL46ngNjS1ORtr78mzFs0xQ+8HHVa24f09j4AACf3YIcP1VYTbBim1FbTYh8R7RC/+ilMrRWo+92HmXnbrRWp9QShUrpUZorQ8C04Av3V+PAb9yf3/ncp9DiO6sfRVNanwkk4dHkpFbhs1iMjpNvvJxAeVnmzApcGpXzfzRyjoaW5wA/Gf1v3Gz2n9JG3IDNAa1BnloDeaeidbFUxOMMk7Ru11pC4R/BDYopfKAbwHLcAX4O5RSXwN3uO8L4Xfa79e6Zkchb+eWMTEhkqYWJw6n5vNjVTjdgdmpIaqPldziapocTgpsMzkcMJObW/ZdUpDP19Hc4HyTz3+Qdc7PO5poFeKyUzedSVI3ojs7336teSXVRrCfPDyKt3NLeW56Ig4nmE3w6y2HaGh2EhsRzNHKOqLDgyitqmdoRDAf1TyA2YdKGmitiQf4msG8n/oX1mYdATAamnmuyXtitf194X98Td1IUzMhLsJ75L5yeyFrdhS2NhSLj2Ty8CgyckuN3jUeJqUID7ZypLKOqYlRzB4/lI32P/LR2e/5FOS1dpdMRibyXNIOkvgjFWnbefrOEUZb4vf2lRnny0SrOB8Z0QvhA8/o2HvkPn9SPGvc2+xNSIhgV0Elz01PBFpLKocP7EtkiI2t+eVstP+R8afe9nkU773oyfPXQ0d/VchEa+/V5ZOxQvQmni39XKtJo9u0EGgf9K/ra8NqVljMJiYPi2Ju1hT6BdbBKd9bF5wekErsos28coH0iyxuEr6S1I3otbz7wHtue2+80f62Z5Jz+6Fyo7rmgWS7ka7x7K16sqaJz8xPkMeD/HjXOPpR51tNvHZ1snx12ueEL9oMYNTkr/6kqEv+HYjeQQK96LW8c+9Jg8NYmJ7DwvQckgaHtdmE4/7f7mTeG3tdKZTSapJjwsjILWNA3wC2H6pgSUYeU1/axpodhWw/VMGXQQsIV+7g7kNdvHZ/ORSsveNzVmwrMj6AsgorWLGtiAW3xXXxvw3hzyR1I3otz2TlUxtzSRzYF4dTYzYpPiusNBYb5ZVUc7ahhbomBwfKqjld18Tfi12Tm81OJ8kx/diQXUzfQAtpH45lnslVG38p5ZK/c9zOC2oer8+5hfnxkYy0uz6APIuepGpGXCkZ0YtezZN7zyqsxKk1t98wgOVbC5g8PIoV24pIGhzGuOv7YzMrlm3K5+sTNcZjHU5NZn45FpNij/NhApTTpxQNuEbwTmVmg76DX7Q83uE1Ld9awOyUjhuTCXEpJNCLXs07925SiozcUsbFhvN2bimLpsSRGh/JvaPtBFjNKAW1zU7jsdX1LWy2/ZSvrY8QYHL6PooHmi2hjNa/50XTfBZPTcBqNrEwPceYJ5BFT6IzSaAXvZb3gqLx8REjD6q4AAAgAElEQVSYTQqbxcTuI1VMSIgwcuV5JdUkRIUYK1w9Ntt+SqIq9S0Pr1vr4pstofwg/PeAa8GTd138qzuKjGt6+s4RRmpJgr24ElJHL3qt9n3jo/sF8u6+4wzpH8yXZWeYmhiFQ0PxqToKy2uNhmSf254gXLm28bvYKF67/1Glg3kqJoMvSl35/XuSBnHvaPs5dfGrP3FNvEq9vPCF1NELv3WhlgQXC4bej/Xu0V58qo5tB8td2+x9XMigsEAy88uJjQjm2Kk6wBW0c23z6KfqfdvpSUOjNjGqZQMtTs2M0AC+KHX9rH2Qh/PXxUu9vLhSkroRPU77ZmLepZCX+9ihEcEE28wszywgNMhKWXUDAEcq6wi2mY0GZP1UnU+jeE+Qv8nhCvITEyLIyC1jbmosq9LGSFsCcVXJiF70ON5lkd4liJ7geaGRfl5JNYumxPHUxlz6Blj4pqaBp+8czq6CSn58xzB+tTmfmoYW4/EmBX/XD/negMzdXfI+x0tojRHkdxVUMiPZzvrsY4yPj5A0jLiqZEQveqSOShB9GeknDQ5jxbYiJg+P5OipOuqbnby85RAmBf+9+SAOd1FNoXsEX2ibifkSJlvzdTTzQ16h2eGqyR9pD2VXQSUzU2IYMTBUJlfFNSEjetEjtS9BHB8f4dNI33ubP6tZ0ezQ1Dc7yTlSxQHLI1i9IvqlLHqq0kHc3PQao+yhlJSdwWJSNLY4GRAawAPJiazYVmQsfPJck+TdxdUigV70OM/+JY/3844bvdjHx0ewMD2He5IG8cL3koyR/uKpCUYw9ZQsvrevjLdzS7GaFU2O1oqzPc4HsSrfgzt4NSBTwTw1OAPr4VPsLztjbBs4KyWGmP4hzJ8Uz0h7mBHcZXJVXG2SuhF+paPFRt4j/bySauqbnZhNitiIYA65UzSXE+QdQBJ/5Ku0L3hqagKBNjNmE5SfbWJGsp3N+08aaSPvKh8hrjapoxc9kif/7p2iAS64w9LLWw6yfGsBZhME2yx8zkNYtL7kvVrB1YDs50k7jDJJz8bcyzMLSIoO46sTNbIxt+hyUkcv/Jr3ZKwnRTNn7W6jbYHnnEVT4vi3jP08khLD+uxjjLSHsrpiNnZOg760PLxTwyP2zew5UkWg1cRrXrXwnolgTzrJ+0NGiGtNUjeiR+ooRTMoLJDlmQVtqm6WZxZQfraBpZvyWTQljk1N87GbThsthC/EaFvgDvKpAX9m95EqHkiOxmI2yTZ+oseQ1I3oEbxXtHpGy57UiGc0vWhKHMszCwCYmxprbKCdEBXCspMLSFSl4GOpJECzguENG4mNCDYWTs2beL3RwljSMuJak83BhV85WllrdHf0LHpanlnA0cpaY/S8q6CSxdMSaHY4Wb61gMYWJ4unJbDm7D+SaPK9+Vgz8L3rNjG8YSMTEyKprG0iwGJi2IA+RqMxTwtjIXoCydGLHsPh1CxMz6F/sI3j1fVYzK3jlANl1VTVNbE8swCnu83kEl5l1kdbMbv7xF+I5+9arRS/SPqEowdOMislhtLTDdyTNIj3847zzHdcG39LLbzoaSTQix5Da01ji+aou8mYUzsAjE25R8eEsd05h3BLHVjxebJVAzXWKEKXFKCAodsLz9nV6d7R9jaBXWrhRU8iOXrRI2QVVjDvjb3UNTnaHB8xsC+HTtQwMyWGf9l3F/30xZuOeWiNK2ffZxD8S37nX7QQXUxy9MLvdDQoOXiihuED+7J5/0n6cWlBvlDFMMb8FlkzdnbylQrRvUigFz3Ci3/Lx6nBanZFck88t5gUB0/UcPeoAT79Hu3+qg0bRsLz+6XJmOgVJEcvrjlfNhKJCLHR2OIkyGoi5fr+rDx2DyGq2XWygtpc60WHLRr4a8B3CX/w/3ZY7y45d+GvrjjQK6XMwF6gVGt9j1LqeuBNoD/wOZCmtW660ucR/stTB+8JuGYTRrdHcAX9ytomgqwmLGYTK0tcQd47TRNiajYqZ7yzN548vAMT5cMeYfqs/3fO88vEqvB3nTGi/yfgKyDUff9F4Dda6zeVUiuBJ4AVnfA8wk95Nx2zmhQnaxpZMj2RvJJqDpRV8/KWQ/QLtvGFZQ5m3dBhNY3n7mmCXbl6XCP4Kh3MzY2vsnhqAk/fOeIqvzIhuocrytErpQYD04FX3fcVMBV4y33KG8ADV/Iconfw9K45WdMIwMtbDnHwxBmWbsqnvtlJZuPDmHXDRVsXfJX2Ber5ani+mk/TCplsWkdqfITRJkGI3uhKJ2P/B/hXwL0vDxHAaa21Zy+2EiC6owcqpRYopfYqpfaWl5df4WWIns7Tu2ZGsus/l/pmJxm5Zdxn2slO22KCaPJpKz9PCsbTJmFV2hg2zh8vk66iV7vsQK+Uugf4Rmud4324g1M7LNTXWq/WWo/VWo+Nioq63MsQfuDZv+SxMD2HV2Ym85uHvsWslBgA7jPt5FfWVxlsqvBpZatDBRr3pcmYEK2uJEc/AbhPKfVdIBBXjv5/gH5KKYt7VD8YKLvA7xC9lHelzZfHz9DicHKgrJoX/5bP/zs5i18GnAZ86DDp/l6LlbzZB0h13++o2ZhMuore6rJH9FrrZ7XWg7XWscDDwFat9SzgY+D77tMeA9654qsUPdbK7YXnpEuyCis4WllrpFKe+U4iWepx5n10M2+XT8euTrsakPkQ5GudVn6Tupu8tHwZrQtxHl2xYOoZ4GmlVAGunP1rXfAcohub+tI2lmTkAa2lk0+s283Ul7YZuXOARVPieGpjLqPSk+in6ozukj71icc1il89cRfrs48B0jJYiPPplAVTWuttwDb37SJgXGf8XtG9nW+hU0Ozgw3ZxQAsnZFEckwYmfnlDAi1tdl1KTJ9MvMouaSdnuqx8Vb0T/n3opE8Nz2RpyfFMz4+os2WgUKItqQFgrhsntG6945OT23MZe7EWGxmxYbsYlJfyCQzvxyTgpNnmpidMsSVK988nWGU+DSCB9cIvoxIiif8itoR/8Bz0xNZsa2ozebfkroRomPSAkFcNu+FTn0DLHxT08Brc24hNT6SkfYwZq7Jpqy6AYCQAAtzU2O5J+t76KwS4OKbgHho4LQ5kiMzs0mNj2S4+/hIe5jRukAmWoU4PxnRiw6dbxJ15fbCNsc8C52OnqqjvtlVOQPwf/7Wtu3vgL4BPH3o0dZR/EWe39N8DKAxcAB/uG3LOYE8NT5S8vJC+EBG9KJD3v1nvPdp9eTXwfVhYDZhbNK9ZkcRSzfl8z9bDlHb7MSsYHD/YDbWzMF+5jQa38slTxPMV2lfkBofSSDwZFe9UCF6ARnRiw55p2Ve3nKww8nOP+0tZummfBZNiSM4wML3bnataq1tdi2U/tl3E3m7YR52k+/lkpVBcXyaVshtrOO9fa1LMHz9C0MIcS4J9OK8PGmZ5VsLmDw88pzqGg9PXxpPpU2gxcRm20+Z99HN9HP4sKrVXS55KiiOt8a/RWp8JKvSxjA0IsQ453wTv7JBtxAXJ4G+F7vYKLm1/4ydt3PLWLOj9fhTG3MZd31/ZqXEGH1pfmddyuGAmXxleZhEVWrUxV+I1nAiIJZXp33O2Kpf4tnvu33+3Ze/MIQQHZMcfS92oTy89+3U+EhutIeybFM+X5bVsP1QuZGrX5ieg0nBOstSJpkOtKZnfFj0BHBQD+avY//I+m1FPDc9EYfz/I/x/gtj8dQECfJC+EgCfS/mPUqenTKE9dnHjMC+cnuhcXvO2t1MSIjggeRoMnJLmZEczYGyal7feYRPnbMIsTW7Ntn28Xm1hjLdj/usa6htctCwtYAZyXbmT2odwbffYcpzzDPxuz77GOPjIyTYC+EDCfS93PlGyd4BdkJCBMs25RNoNTHSHkpGbikZuXAgcA7B7XZ6uhBPRU2Z7sfdptWcqW3GalKMtIfydm4ZN9pDmT8pvsMKn/Z/YchqWCF8J4G+l/MeJa/ZcZi+QZZzRtZF5bUEWk00NDtpcTrZZfshduVbd0lvJ2yx3HpmGdMSo5geGshfPi+lscXJt2LCeCDZfk5qyDuAX6jtsAR6IS5MAn0v1n6U3DfIwrJNroVOuwoqie4XyOb9J7lr5ABem3MLz7yVx+unHnWVS/r4HEYb4dBhzHK+xLTEYHKLq7lrZCBr597CprwyPi08xdIZSXxZVkNGbmmH+XdpOyzE5ZNA3wOdr5lY+5z2xR7rGSV7jnse+/KWrxkzNJwN2cXMSolh6Ywk9r8whU8acn3Kxbv344brJ6Mee9f4QJmdMqjNPAC03RFq+6Fyyb8L0QWkvLIHupKa8qOVtSxMzyGrsMII7AvTczhaWcvK7YWMtIcxf9L17CyoYGJCJBuzi8l6fgIjG3J9XvTUSAA8Xw2PvQu0nQfwNDXz5v2XxdN3jpBt/4ToZDKi74EuVC1zMfeOtvN+3nEWpucwNzWWtVlHjOPgCvoAi6cm8EjWXQwMqPKpjbD3Tk9Lkz7iBa+fXaxaRvLvQnQtGdH3QJ4FTd6jZO/jF+JZddrscLJ8awHNDier0sacE1Dn7f4uA3WV760L6M8Y81vkpeXzwveSjJ/5Mlp/cnK8NCwTogvJiL4HShoc1mbkvTbrCGuzjrAqbYxxzvny+Ks/KWJCQoRxzOnUHCirNnq5/7XfSww+vRuafRzFa6hU/Rnb8AqLp56blpHRuhDXngR6P+W96jWvpBqzCVZsKyLAYmLbwXICLK6a+PSKHxD+UX3rDKsnTeNDkFfXT2ZJ6C/ZkF3MxISIDtMyUi0jxLUnqZseKK+kmlVpY5ibGsvyrQXMTY1lVdqYNjsseefx1+48bHSZPNvYDEBji5P1FQ8Srupb92rFt1G8J8hnTXydzftPMislBovZJJOoQnRTMqLvoQ6UVbeZ4OwbdO5b6V3tAq4ukwNCA/m78wFM7oB+KQueNFBjjWL/w5+5yjPdbRIAIxUjaRkhuh8Z0fdAZhMsc4/Qn75zBIumxLFsU77R+RFgztrdLMnIY332MWIjggGob3aSWeMK8r5Msnpo7fpqDBzA/oc/M0btnrSMd2mnTKIK0f3IiL4b855Q9dwG16rV56YnsjyzgI/zy8k/UXNO58fquia2HSxnVkoM05Ps3PzGMAKU64RLGsVrOBp2C/ee+Sk0wCq47NJOIcS1ISP6bsx7YZSn0mZheg6DwgIBaHY4ySqsZHbKEEba2y6WShwUSoDFxMbsYsakDydAOX0rldSteXit4VM1irL73zQqet7bV3bRBVBCiO5FaU9j8Gto7Nixeu/evdf6Mrql1vYBQ4zFTbffcB0ZuWUE28zMm3i9cbx9Pbzz+TCU++31JcCjoMoZxJ/v2IXDifEXhKe1gqfNgucDSEb0QlxbSqkcrfXYi50nqZtuzNMH3ruN8OfHqsjILcOkwGxqjd5NLU5e/Fs+7/xoIuAO8viWptEanAoSGjYyMyWGGCfn7O7k/V3aBQvRs0jqphsrPlXH0k35rNlRxOKpCaz6pIidBZVYFDg1DO0fzPKtBYwe3I+mFicRITZ44z7wBPmL/H7PJKtTQ3zDRh5Ijmbz/pMX7JlzoQVQQojuSVI33Yz3BOySjDxjw+0Qm5naJgcAs1JiOFHdQGZ+OcFWM3XNDmalxLDw6E+IOb3bpxbCWkOjMvNI1LvkFlcTHmxFKcXdowZQerqBdXPHdeGrFEJ0Bl9TNzKi72a8J2Bj+ocwLTEKwAjy0xKjcGrYfaQKBdQ1O/hD4K/45b5JPgV5YxSvLKRP28Pfi6uZlhjF6Jh+LJoSx8bs4jYtEoQQPd9lB3qlVIxS6mOl1FdKqQNKqX9yH++vlPpQKfW1+3t4512u/1i5vdBYQeq57ZnsfGVmMgvTc/jkUDlZhZVtHrfj6wqOVtaxx/kwRQEzORw4k3E6z+dUjVPDDc43yU47iMMJz01PJLe4mqToMFb4sEG3EKLnuZIRfQvwE631DcB44EdKqRuBnwGZWuthQKb7vmjHe+R+tLKWJ9btYWF6jpEfb2x2kFVYSX2zK+rGhAcB0OTQvF58d2u5JD6WTLqD/GNDPsBqNhnPNX9SfJtSyfmT4mXBkxB+5rKrbrTWx4Hj7ts1SqmvgGjgfmCK+7Q3gG3AM1d0lX7IuxfNoLBA6pudBAGfFVayZkcRTQ6NWYFDYyx6GvrGWOyqCri0Va07nCN5tHkJJgUP9Q/mh99OYGF6Du/tKwO4YK94IUTP1yk5eqVULJAMZAMD3B8Cng+D6zrjOfyRZ+HRgbIz2MyKFqdm+dYC6pudBNvMxEaGEGAx8e6+49z05njsyrf+8NA6ivcE+diIYJwath8sN3rSA7KzkxC9wBUHeqVUH+DPwD9rrc9cwuMWKKX2KqX2lpeXX+ll9EjeOy9ZzCaaHa0VUD++YxiZP5nCl5bZ5PEgfZrLL2kUv0uP4vrGjTzavISR9lAqa5uwmFp3gkqNj2RoRIiUSgrRC1xReaVSygq8D3ygtX7ZfewgMEVrfVwpNQjYprUecaHf48/llefbAOS9fWV8cOCk0f3xiXV7jHy8zawIsJrJ4RGsOHwrl/S6/bl5NP9Q+ww2iwmzgpuHhJNX6greHe0mJYTombp8ZaxSSgGvAV95grzbu8BjwK/c39+53OfwB+fbAOSukQOMIP+TP+7D4dQEWU3cPCScwaXvs1j/Hqu6eJD3fE43KzPDG9KZmBDBroJKRtpDOXaqzmiXsHhqAuPjI6SFsBC90JWkbiYAacBUpdTf3V/fxRXg71BKfQ3c4b7v97zLJT28yyWf2pjLwRM1Rnthz76qT23MZWBoAM0OzdN3DmdDyjF+aVpDtKrwKch/o/ozUv+B4Q3pjBjYh50FlcxMiWHT4kksnpbA27llzEi2sz77GNDxjk9CCP92JVU3Ozl/6fa0y/29PZX3yD01PrLNptje3R5nJEezYlsR6z89xjc1Dbw25xbySqr53ek59PmoHK3AepHn8uzVetYWReHDn2FOz8FmMXHwxFkmJkSwef9JYiML29TF/2BsjPSkEaKXkhYInci706R3V8f2xycPjyQjt4z9tscIMTWjcG/P58NzaKDRaWLekL+xfl4KK7cXYja5do+6rm8gNY0tLJoSx66CShbcFnfO3ICnE6UQoueT7pXXgPfIffHUhA5H9n2DLCzblE9+4BwCdLMR3C+apnH/o1GbmDdkM7sKKlizo9DoU28xm3jhH24COO/IXTblFqJ3kkDfSTwj6/b7uO4qqGwzsj+8dR15/f5EQEOTz+WSDnMQheOX8g+7BtPidPJA/2Cemx7Fsk353GjvC7StppF9W4UQ3iTQXyJPj/j5k1rTH2t2FPKnvcUUldfy3PRE5k+KN0buz01PNAJu3d7f81+mNZgb6n16Lg00htgJvOs/2Fo1hlVprRuBzJ8Uz5dlZ4yKGu+gLiN3IYQ3CfSXaEJCBMs25QMwf1I8a3YUsmxTPt9OjOLhcTGs2FbEx/nlfFFa3dog7JUUdEU+0/AtDw+uIF9jjSL0p18B8KTXzzx/HWw/VCGtC4QQFyWB3gfei548I/mlm/L5XdZRSqrqjVE8QE19C8u3FmAzK0baw0jdPB1dke9zj3jPiScI5/DDn5HawXnt8/6yy5MQ4kKkH70PvDtNrtxeCIDFpCiuqmf4wD6MtIcZdfRrs44w0h7Kx+ZF3Pq7eJ+CvKcvTa2y8pvU3Ywxv8XhtL3nDdqyy5MQ4lJIeaUPPBOtK7YVMXl4FBm5pQBE9bFRfrYJm1nx0++MYHlmAQB7Av+RgIaTPo3i67SNnzXP413nRCYmRLCzoJLFUxN4+s4Ldo0QQgjZYaozJQ0OOyfIA0wcFoXNrGhyaDZ8dow/8zR5PEigD0FeAyXOSP5dLyB2yhxsZsXOgkpiI4JZn31MOkgKITqNBHof5JVUc/eoAbydW0pYoGtaY5Q9lIzcUqYnDWJiQiQran7EMEp8nmwtIoaJTcsZccfjjI+PwGJ2vRVmk5J2wUKITiWTsefhPQFrNsHG7GJG2kPZX3aGUV7fFxyYRaIqBZOPi56AU0Fx/Nd1q1iSEMGKbUXcMLAvZpNiibtKxzvnLpOrQogr1SsC/flaBbdvB+B9nmcCdtGUOH6fXcy3YsLILa4mLNDC7yp+QHhgPZwCLmEjkArVn7enfeSqr0911eJ7qnQWT01oU5svtfBCiM7SK1I33lUz0Fqe6NmftaPzVn9SRHJMGMs25RMcYCa3uJoBoQF87HyMcFVvbMZ90f1acQX5Mt2PZTdktGk05r3xiOTlhRBdxW+rbtqP4rMKK1iYnsNN0WHkn6g5b82550PgxkGh7CyoYFR0KPtLz/Bp4I8YqKtcI3gfr0FryNfRzNC/ZuzQ8DYVNe1r4dvfF0KIi+n1VTftR/EAzQ4nWYWVzE4Zct5g6mlMtrOgwpWL9wryyscg7xnF5+to7m76PzQ7NDsLKpmRHM367GOs2VHI6k+KpBZeCHFV+G2O3hM4Pe2B12YdwWo2sWBSHGt2HKZvkKVNTtyTrpmQEMH67GPMSLbz8wN3u3Lx2rc8PLiC/AlbLNMaXqSuyUFYoIXqhhasZsUPxg7mRnvfc3rgeF+zjOaFEJ3NbwM9tG0bbLOYWDf3FlLjI9lfVs3STfl8WljJ63PGGWmdvgEWth8s57npiTyUOYm+Jlcu/mLDeO/WBaeC4niyz//F3FTLxITI1r8Mys6wdNOXHK9ubO2BI4QQV4FfB3rPZOdIeygHys5woMxVrnhrfARb88vZ8XUFL285yNqsIwAkDurLlvqHCMlsBnzvEV+lg3jiurfIP1FDQ5WTbw+wMcoeysbsYmYkR7P9ULkR9NtX1wghRFfz20DffnLT02Xyy7IzbD9UwZLpifx6yyGjAdm6x8cxJv1GbKZmnydba6xR/OG2D1y7O9U2YzGbCAROnmng4/xyo9mZ57k9OXrpNCmEuJr8NtC3b/zVvn/7SHtraeWrpl9ya/oBwPeKmobAAWy8dTNPtquFB9x7w9qZPymerMKKdnu3DpbqGiHEVeW3gb79vqje/dtXbi9iwc4JfGVuBjOuyVYffqcGVEAYWQ9+7grWg8Pa1MJ7UkDedfHtP3BAdoASQlxdfhvovbVP4yzMmkiw136tPk224srF/1fcO2x3/y5o3Z8VMAL9+PiIC/aIl+oaIcTV1OPr6D194L1lFVYwZ+1u43heSTWfhDzLrenx6OfDCMb3/Vq1hnpl49NHC0lxvE5GbplRh+89Ws8rqWZV2hhWpY0xRutSFy+E6A56/IjeszCq/QrTRVPijONPfjETfeZrn/Pv0FpRU6ut/P72zxgJBFrN3BIbZkyoeqeHvG97L4KSkbsQ4lrzixYInuA+O2UI67OPGUG/4VfDCWg4Cfg+yQquUfwO50jmtCzh2e8mUlReywcHTrJoShwO57kfLkIIcS34dQuE9uma1PhIJg+PZPnWgtb2Bi8lGhuA+Ny2wP21wzmSR5uX4NRwpKKWoREhLJoSx4ptRUb/HEnLCCF6ih6Zumk/ol6zo5C3c8sYaQ9lUNa/4fw0E6UdPveHB6h1WrnVtIGahhYAZiTb2ZR3nA3ZxUxMiODL4zXn9KaR0bwQoifokYE+r6TayMFPHh7F27mlzEyJYXrxr7mVLSgfslFaw6ngOCKeyWVJRh4bsosxKVeQX+Je6PSDsTE8+lq20XVSArsQoifqkkCvlPoO8L+4qtRf1Vr/qjN//+b9x/n65FnuGjmQjNxSVvffyNS//xWzcvo8ij+oB3N31S+5ZWUWe45UYTFBixNmJEe3aVEQZLNwU3SYrGgVQvRYnZ6jV0qZgd8CdwM3Ao8opW7szOe4J2kQdU0OMnJLWdFvA3fUvo/FxyCv+gzi07RCfmB6GaVg9xFX++Egm4XFUxPYfqicrMIKY4J3VdoYNs4fL/u4CiF6rK4Y0Y8DCrTWRQBKqTeB+4EvO+sJRtrDyLXNo5+qg3rfdnkCaAwcQOC/5JMK3Dd6EBuyiwFwatf9p+8cYSx0umvkgPP2i5dRvRCiJ+mKQB8NFHvdLwFSOvMJRqUn0ddU51s1jYa/Bn6Xsom/ZMW2Il4prOBAWTUbsouxmBQp1/dnz5FTbMwuJjYyhPmT4s8b0GUCVgjRE3VFeWVH8fec6VGl1AKl1F6l1N7y8vJLeoK+1PqUpnFi4k11J38e9GNWbCti0ZQ48kqqeXO363PombtHsGH+eNY9Po5Aq4n3844DroDevleOEEL0VF0xoi8BYrzuDwbK2p+ktV4NrAbXgqnOvAANfBh0Dz+pf5RVaWN43b1idmF6DknRYZSdbjAqa8AV2F+bc4vUxQsh/FJXBPo9wDCl1PVAKfAwMLMLnuccGlDKzN+ve4AFR/8Bm6XtNk6NLU52FVZ2uPmHpGWEEP6q01M3WusW4CngA+Ar4I9a6wOd+RwqIOycXJDRQnj2IZ6oeIQZyXaaWpzMe2MvL285yLw39tLU4jQ2/5DqGSFEb9Eje908+5c8/jXvLvpRZxw7TTA/iX2HvxdXGz1pzCZYuinfOMeTrmnftlgIIXoiv+51A3Ab6/g0rZBP0wpJ4o+kOl6nsrapTU+akfYwbBbXS7RZTMauUtKrRgjRm/TIQP/C95JYlTaGpzbm8llhJQAWs4nJw6JcJZTujUAWpucQYDGxeGoCARYTC9NzjJSNVNYIIXqLHhnowRWoZ6cMYfnWAuamxjI3NbZN98r39rkKfValjeHpO0ewKm0MgHFcCCF6ix7Z1Ay44F6t4+MjGBoRwqq0MW1Wtnp2fxJCiN6kR47ovSdTx8dHGMfHx0cYPWk8feO9SbpGCNEb9chAL3u1CiGE73pkeaUQQoheUF4phBDCNxLohRDCz0mgF0IIPyeBXggh/JwEeiGE8HPdoupGKVUOHL3Mh0cCva0Vpbzm3kFec+9wJa95qNY66mIndYtAfyWUUnt9KS/yJ/Kaewd5zb3D1XjNkroRQgg/J4FeCCH8nD8E+tJz3moAAAPxSURBVNXX+gKuAXnNvYO85t6hy19zj8/RCyGEuDB/GNELIYS4gB4d6JVS31FKHVRKFSilfnatr6crKKVilFIfK6W+UkodUEr9k/t4f6XUh0qpr93fw6/1tXYmpZRZKZWrlHrfff96pVS2+/X+QSllu9bX2JmUUv2UUm8ppfLd7/WtveA9/rH7v+n9SqnfK6UC/e19Vkq9rpT6Rim13+tYh++rclnujmd5SqmbO+s6emygV0qZgd8CdwM3Ao8opW68tlfVJVqAn2itbwDGAz9yv86fAZla62FApvu+P/kn4Cuv+y8Cv3G/3irgiWtyVV3nf4G/aa0TgdG4XrvfvsdKqWhgMTBWaz0KMAMP43/v8zrgO+2One99vRsY5v5aAKzorIvosYEeGAcUaK2LtNZNwJvA/df4mjqd1vq41vpz9+0aXAEgGtdrfcN92hvAA9fmCjufUmowMB141X1fAVOBt9yn+NvrDQVuA14D0Fo3aa1P48fvsZsFCFJKWYBg4Dh+9j5rrT8BTrU7fL739X7gd9rlM6CfUmpQZ1xHTw700UCx1/0S9zG/pZSKBZKBbGCA1vo4uD4MgOuu3ZV1uv8B/hVwuu9HAKe11i3u+/72XscB5cBad7rqVaVUCH78HmutS4GXgGO4Anw1kIN/v88e53tfuyym9eRArzo45rclREqpPsCfgX/WWp+51tfTVZRS9wDfaK1zvA93cKo/vdcW4GZghdY6GajFj9I0HXHnpe8HrgfsQAiu1EV7/vQ+X0yX/XfekwN9CRDjdX8wUHaNrqVLKaWsuIL8Bq31X9yHT3r+rHN//+ZaXV8nmwDcp5Q6gisdNxXXCL+f+0988L/3ugQo0Vpnu++/hSvw++t7DHA7cFhrXa61bgb+AqTi3++zx/ne1y6LaT050O8Bhrln6W24JnLevcbX1Onc+enXgK+01i97/ehd4DH37ceAd672tXUFrfWzWuvBWutYXO/pVq31LOBj4Pvu0/zm9fL/27djlAaiIADD/6sCdnoEm7SWKSwEuxzCxmOk8hCewMLCRiStF5AUIRGRRBttbK0tnsWbgE0gYMKS4f/gsctWM8wy7M6+BWqtX8BnKaUfl86BF5LWOHwAg1LKQdzjq5zT1vmPdXV9AC5i980A+F6NeP6t1rq3CxgCC+AdGHUdz45yPKW9vs2AaawhbW79CCzjeNR1rDvI/QwYx/kx8AS8AXdAr+v4tpzrCTCJOt8Dh9lrDFwBr8AzcAP0stUZuKV9g/ihPbFfrqsrbXRzHf1sTtuRtJU4/DNWkpLb59GNJGkDNnpJSs5GL0nJ2eglKTkbvSQlZ6OXpORs9JKUnI1ekpL7Bcc9NqcBRI/8AAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 13, Loss = 4.360390763914505
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 14, Loss = 4.1166477268856685
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXoAAAD8CAYAAAB5Pm/hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4wLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvqOYd8AAAIABJREFUeJzt3Xtc1GXe+P/XNTMMJwURyARRAlRKF5c0NdQ0rbbW2rKtPaikHdTc9efe6x7a9D7s7r267d677X37tdvUSgul2trs5F3ZYh6SwiSUtNAYPICjBqioIKeZ6/fHzOfjgKijgMLwfj4eLDMfBuaaxn1z8b7e1/tSWmuEEEIELsvVHoAQQoj2JYFeCCECnAR6IYQIcBLohRAiwEmgF0KIACeBXgghApwEeiGECHAS6IUQIsBJoBdCiABnu9oDAIiJidGJiYlXexhCCNGp5OfnV2itYy/2uA4R6BMTE9m+ffvVHoYQQnQqSqkD/jxOUjdCCBHgJNALIUSAk0AvhBABTgK9EEIEOAn0QggR4CTQCyHEFfbsJge5joom13IdFTy7ydEuzyeBXgghrrC0PpHMyS4wg32uo4I52QWk9Ylsl+eTQC+EEG3In9l6RnIMSyanMye7gKfX72FOdgFLJqeTkRzTLmOSQC+EEG3I39l6RnIMU0f0ZfGGYqaO6NtuQR78CPRKqReUUt8opXb5XOuplPpQKfW193OU97pSSi1WShUrpQqVUje228iFEKIDOt9svbCsqslMP9dRwcrc/YxKjmZ13sFz/gpoS/7M6FcBdza79hsgR2vdH8jx3ge4C+jv/ZgJLG2bYQohROfR0mz9QGU1s7LyyXVUcO8zHzP9hW00utz0jQ5jyeR0Hl31Gfc+83G7jOeigV5rvRk41uzyvcCL3tsvAvf5XH9Je3wK9FBK9W6rwQohRGeQ66hgdd5B5o5PMWfrG/eUU1vvYlZWPlU1DdS7NHWNbjbuKWe3s4raBjfR4fZ2Gc/lNjXrpbU+DKC1PqyUusZ7PR4o9Xlcmffa4csfohBCdB5GTt5YXB2ZHM2c7AKiwoJocGtcdY2cqm1kq/0nxKkTUAv8Ex4Ij+HV69a3y5jaejFWtXBNt/hApWYqpbYrpbaXl5e38TCEEOLqWL65hNnjkshIjjErbWaPS6JbiI0gi8KtMYO8UpgfPVwVTP/krnYZ0+XO6I8qpXp7Z/O9gW+818uABJ/H9QGcLf0ArfVyYDnAsGHDWvxlIIQQnc3MW5KYk13AoLhI0vpEMisrH4C5E1JYc/Q+wlUD4AnuvhQQUnu0XcZ0uTP6t4Fp3tvTgLd8rj/krb4ZCVQZKR4hhOgKfKtuntlQTKPLDcCUnJGEqwZzBt+S9prx+lNe+TLwCTBQKVWmlHoUeAq4XSn1NXC79z7A/wElQDGwAvhJu4xaCCE6KCNdM3VEX7Y6Kvmnmk0hPyBU1583wLe3i6ZutNY/Ps+XJrTwWA38tLWDEkKIjubZTQ7S+kSauXdjA1RhWRWPj00m11FBYVlVk3TN9pA5ROvjnsXLiwR5reG0PZbu7TD2DnGUoBBCdHQHKqt55qNilmUO5UBlNYtzvkZrzYBru2O1wOKcYu5O601an0hec89joCqDC6RpDEa65rQ9ljWjP+Dxdhi7BHohRJfnO1s3GDP0x8cmA3DPkDjeLTzMrKx8bru+FzX1LgC6B9sI/uDXFFg3YC10QyFguegEHvAE+Wp3EMtHb2XeHQPbJciDBHohRBflG9yN2frcCSm43DRJv5Qeq2bhpDQykmNYljmUqc/lsbbgEDYLWJTi9v3/Rab1n5eUfzdm8dXuIP5t0IdsyjvIyOTodut3I4FeCNElGc3HlkxO554hcby1w8nCdUVMSo/nmY+KARieGMWaPM8e0ISe4Xyw6zBub5TeYZt23lLJC9EavlE9GVm7hPkTU/nbmORzNlm1NQn0QoguybcMcuqIvlgtCrvNwtqCQ4QEWXhh+k1kJMewYG0ha/JKCbYq6lwai4IvgqcTphsuaxbv1FGMqlvCpPR4ZoxJbjKWwrKqdgn00qZYCNFl+TYfu+36a7C0ELgXTkojLjKEOpdmq/0nOOyTCePSSyVVTCqfZDq4TS+lX88wNu0tb9KxMiM5xlwPaGsS6IUQXZbRfGxSehxrC5xYlGLu+BSCrBaz0+SCtYU4q2r5JOSnZ9sWXOTnajwpGuNzZWgSuXetY1ZWPkopMlKizb8m2rM9sUECvRCiy/A9/cnIi88el8SnJccItlmwWhTlp+uYOyGFRpebR1d9xi8K7mBfyGSu5bhfpZJuZeXvfIdPHnLwSaaDG9yvMOz4H1i47itcbo3VorhnSFyTdE17U549TlfXsGHD9Pbt26/2MIQQAe7JNwp5t/AwyzKHsnxzCfE9Qnh752Gu6R7MN6fq+N6Q3uxynqSkvBqXW/MxDxOlavxK02gNZ5Sdl279tEmpZq6jgmkvbKPBpZvk/tuCUipfaz3sYo+TGb0QIiCc76zW6Su3Nbne6HLz2IvbKT9VR3ZeKfWNboZf15O5E1LIzislKaYby/g9uy0/JMpy8SCvteejWgfxn2k5PD42+ZxAbm0p+X8FSaAXQgSE853VOiol2rx+z5A4AGrqXex2nsSioK7RTW2Di6UbSxiVEs2kXT/hZnah8CMXr8Gpe3C9+xVevj2PftHhTb6e66hgVlY+QVbLObn/K0nKK4UQAaF5ueTqvINmXfqguEjzui+XhsFxEawtcLI57DcklB4Eq3+LrQBHVBSvjvqAoNz9LM7xtEfw9c5OT5f2ZZlDzUNIZmXl885OZ7seBt6czOiFEAGjpbNam19vcGmCrJ5Q/rn9Ud6pvJt9IZNJcB30r6JGw0nCSePv7Mvczrw7BpoB3gjshn7R4WaQN8axLHPoOTP/9iYzeiFEQJi+chvxPUJ4b9dR86zWyuo6Dp2oZeYtSazOO0hidBj7K2uwWxU7Q2YQoc+czcH72XzsuA7lwYhslt03GPCsDTw+NpllmUPPqaBpqS4+Iznmis7mQQK9ECJAxPcIYU1eKVNGJDDvjoFUVtexJq+UlNhwZmXlsyxzKO/sdPLuqQcvuXWBBvaEDuWu479g8ogEHuzpmZHPyS7gO4N6keuoaBLAmzdEu9okdSOECAgJPcOZMiKB7LxSfvBsLtneoB8ecnY++9vC2wi3NPiVovF1IOIm7jz+C+5Lj+e9XUepqWts0ienpUVgo199RyAzeiFEh3G+wz2Wby5h5i1JwLkHffjOmiemxfH10dNs23+chKhQJqbFkdAznB9+OYceL+V6+sNfyoBiUsm9ax2PrvqMfj1D2LS3nLEDYli8oZi541PMGfz5FoE7Cgn0QogOw7ejZPODtY3byzKHNun2aDhQWc3T6/fQ4NIkRIVSevwMU5/L4/2ef6VHdb5/m558bhwLS2KPN8jXNriZerOnYmfRuiImpcex2qe1sO9ir+8vgI5CAr0QosNoXiJpOHWm0bz9zIZiCg9VnbP4WXT4JPUubfaJ/9z+KFHqDJz2/5Sn4+5Q/nH7VsAT0ONfL6S2wc38ialmieb8iam43PDgsIQmv2xW5x00F4Hbs7f85ZBAL4ToUJrPjoFzbhvlkcasv9HlpkeYnQmpseQUlbP29I+JUmf8bl1Qo+yMZDVzb/ccPPL42GRezy9jz5HTDE+MYsaYZJ7d5DgnJbNkcjrv7HTywe6j5tdGJke3a2/5yyGBXgjRoRgdJeeOT2Fl7n6AJrcHxUWw23mSR1d9xowxSTS63JxpcBPh1vxPyXcJD/avokZrQHlaFwyuW0VIkJtBcZFmD/o9R04z8NpufLb/OCu2OM5bKllYVtUkqLd3b/nLIYFeCNFhNM+9G8G9e+jZUHVfehwl5ac50+Bm8YZi7DYLQVZFTt2PCFf+HQaiNWxTafyw9jfYrYq545NZmbufWVn5DOnTg4+LK5gyIoGFk9JYscXBonVFAOZBIb46Sq38hUh5pRCiw/CdHReWefLwyzKHsrW40rztcsO8OwaY37OA5/jKNsUsm7wQowHZ57Yh/LD2N9gs0ODSdA+1sSxzKA0uNx8XVzA6JYaFk9IAT3CfPzGVrcWV7fnS25W0KRZCdCo3/zGHilN1KItiAc/xkJ8Hc2sNp1Q4P098kw1F5dwQF8HBYzV8b0hvc/fsrKx8vhUfSdGRUx0qx34+/rYpltSNEOKK8K2RN1zODtJwu5V1tkc8FTV+9qYBOK7D+OV1b7KjtMqsnDHKOWePS2JOdoHZl6a9D+u+0iTQCyGuiAOV1TzzUXGTYDorK5+703qbj7ngL4P9P4d9m/gQPAHez1l8nbJzE6tpdLsZUF3fYuXM8s0lHX5BtTUkRy+EuCKMXvCzsvJ5ev0ecwOUcR3O31N+/LYZ6H2bAM8M3p+6eE+QD2bVrZ+yLHMoNquFG3pHnBO4M5JjWPXw8Bavd5ReNa0lM3ohxBVhtOh9ZNVnnmoZq2LVI8ObbHpavrmE2ePO5soTnevYFPwa3aoP+926QAO74h7g0+vns3RjCUu8fyG01F2yq2hVoFdK/Rx4DM9/2y+Ah4HewCtAT+BzIFNrXd/KcQohOgnf9Mv0ldsYlRLNoLhICsuqSOsTSaPLkzSvd2l2O6uatDq4KTGKv334NY0uNzH73uK3wc9jr63z63k14MJCef8f860p/8u3wHxeo9wxENIwl+OyUzdKqXhgLjBMaz0YsAI/Av4E/E1r3R84DjzaFgMVQnRcvue1GumXFVscWBQsXFfEYy9ux2qBh1d+RqNbMzolmtAgC4vWFfHa9lLz50SG2vmQWeyx/Zj/sf8vdu1/kD9JONsyv2ZiySRzLIGUfmmN1ubobUCoUsoGhAGHgfHA696vvwjc18rnEEJ0cL659YzkGGaPS2LRuiIiQ+2E2a3U1LtYvqmEukY3U0YksPqxkTw//SZsVsXaAicPZyTycEYiv9x9L3HqhH8nPfl8qOBIIn/rbLKIKs667NSN1vqQUuovwEHgDLAeyAdOaK2NDkRlQHyrRymE6NAKy6rMEkWjVe+olGjWFhxi7vgUPi2p9LYODmHhpDSe3eTAagGbRREXGcrI3Ee4We8Ci39thDXwKd9CZ77Z4iJqV03RnM9lB3qlVBRwL3AdcAJ4DbirhYe2uCNLKTUTmAnQt2/flh4ihOgkjBm90at9dEo0W4srmZQez3Mf76Om3kVsNzulx2tZsLaQw1W1bCgqx25VLHH9jsF6l3+nPQWFwj2LUWk/YNcWB1s3l0hQ90NrUje3Afu01uVa6wbgDSAD6OFN5QD0AZwtfbPWernWepjWelhsbGwrhiGEuNqMdM2bBU5Se3Xj4+JKJo9I4Ia47tTUuwizW5k5Nolgm4U1eaV86TzJe/Zfscf2YwbXFfhVLukkhr3DF0LaD8h1VLB049nDSMSFtSbQHwRGKqXClFIKmAB8CXwEPOB9zDTgrdYNUQjR0T35RiGLc4q5Lz2eoqOnGZ0Sw9s7D7M4p5gpIxJ4btowXG5Y+fBNWC2KlbVzSVWH/M7FnwqKZX9mHj/6tC9Pr98TULtWr4TLDvRa6zw8i66f4ymttADLgSeAeUqpYiAaeL4NximE6MC+PHySugYX//zqKHPHp7Cz7AR1DS6CrIq3dx4GPF0eB75+O8VBPzaD/IUYC611Ib2IWFDcpE/91BF9JchfglbV0Wut/wP4j2aXS4Dhrfm5QojO5e603hSWVmG1uAFodLlpcGn69Qzj+aMPEpVVgwZ6aj9bFwDqurHkjn7BM3v3lkt25FOcOjJpgSCEuCy+tfMv55UyPjUWl/acAOXSMD41lpXlPyDKUuNpW4B/h4EYQZ5pb5vlku/sdJrpmnl3DDSPGzSeX1yYBHohRBO+AdyQ66jg2U2OJtd8a+eVgpyicuobPTP6jyyP89y+24mk+pJaFxy09mWo9XVWJP3NfL6M5Bj6RYeft+mYuDgJ9EKIJg5UVjMrK79JY7FZWfkcqKxu8jjfg7xDg6zm9U9Cfur3pic424DsiD2Rfv/+hbnZyuoTnR4fmxzQTcfamzQ1E0I0cc+QON4tPGw2FttRegKrRZldJn17yPsukO61TyZIAX7m4fE8lMrQJP424EWy80q579UCNu2tMPvFi7YhgV4IYTYfmzEm2ez0+NDzeeQ6PMfnLZiYes6BHMbu1tV5B/k6ZAo2fxdavYdyA6iYVGLm5LEQqKl3sbbAydzxKS2ezSounwR6IQQWRZMDsNcVOvGm27HbLCzOKeajonK+OFRlHhyy21nFdz8cz2OWE4B/PeIBaq3deXHspiZpl1xHBZv2VkhFTTuRQC+EoFdECEFWxaJ1RbyeX8aeI6cBGBTXnYPHzlDX6CbXUUlI0NnE+X05txGjTviXh9fg1D14dfR65t0xkMd9vtb82L6RydGyIaqNyWKsEAHIt3LGuO1bOdO8iuaeIXEEB1lRCjPIh9mtLJh4A3MnpFDf6KZX92DeUr/k5qxk9G8jieGYf+WSGpw6il8lvMrqvIPnVPQUllVJRU07k0AvRADyLX00DvaYlZVPWp9IcwZ9oLK6Sd/27w3pjdunBeGkdM/i69KNJUwZkcCahn9hgCo7WxN/kTFoDQ0arqvL5v9uzyF7xsgW69+loqb9Ka1bbC55RQ0bNkxv3779ag9DiIBiBPSpI/qyMnc/AGnxkRR68+wAc7ILmD0uiVe2leIorz7nZyTHhrO4exYDnW9gxe13uSTeID894QOzasf3UHCjake0jlIqX2s97GKPkxm9EAHKt/TRONhjq6OSBm/dou8BIUdP1gIQbLPQLzrMrGGfcep/ucH5OjZ/g7wGp7sHA12vsH2ag+wZI3lumicOvbPTaT6vBPkrSxZjhQhQuY4KszeMMaM3bs/KyufhjERW5x3kvvQ41hY4sVkUdpuFhKhQPjh1P8HK7VdNvG9SwKl7MDNmNcHHasxrXf1g7o5AUjdCBCDfShbAPHw7KTacwXER/OPzQ9Q2uJmUHs8Hu49gt1r4SE+jBzXeZjN+7mrVsEf34c76PwMwZUQCCT3DzTUCqZxpX5K6EaIL861kKSzz5OSXZQ4lOtzOmrxStIZBcRGsLThETb2LT9Qj9KDGbDzmz0KrBop0PPc0/hejkj2Hfb+98zBpfSKlcqaDkdSNEAHINwfePB/+ackxaupdnDzTwO9sLzDFugGr278cPHgC/I5rv88Pyx5EKXhgWDx/vD/N7Inzzk6neW6rzOY7BpnRC9GJ+dtp0lBYVsVz04YxPDGKx049w0O2f2JT/lfTNGLhSP8ppM9+ge8Pjcdus5g9cIxcfL/o8Fa+KtHWJEcvRCfWfFdp8/stqf/tNQTpOr/z8OBJ1dQpK59n7m3yc6VU8uryN0cvqRshOoFnNznM3Lch11HB8s0lzB6XZNbLr847yOxxSRSWVbUY6I0gf0nNxzQ0KCshvz1GRrPHSHqmc5DUjRAdlG9axqhiWbHFYV6fk12ARcHinGLGDohl8Qbv55zic3rH8+48+F1Pgrh4kDf6w59U4VxXm809Me8ysDaLFVtabp8gOj4J9EJ0UL5tDHw3N+05ctJMzzw2JgmXW7O24BDDE6NYW3AIl1ubeXPAE+S3Pw/adfFqGuClxtu4J/pdbrW+yKT0eHYfOsn41Fi2Fleav2DS+kS250sXbUxSN0J0UL4nOF1/bXcKD1WZm5vmjk8BPLtNrd6NTtv2H8dus2C1eMP5u/MgfxXajwAP4FZWXtO3seNbT7K7wMn8ianMGJPMDXHdWbSuiPvS46Q2vpOSGb0QHZjRxmCro5K6Rjf//OqbJrtbAeZOSMGI7Rblud8954lLmsXXEswwy6skZP4vA6+NYP7EVJZuLCHXUcGMMcnmL5ipI/pKkO+EZEYvRAdmtDGYlB7P2oJD2CxNw3ZSbDiLc4oJslq4sW8UPy39BRk5u/z++RqoJogpsW+w5M7UJourg+IizQ1PcihI5yaBXogOyrdUsrCsigUTU/nr+r0s3lDM3PEpjEyO5k/vF7GM33Mzu+AQYPH/QO4dvb7PQ0d/SKPLzX29I1psFQzIoSABQFI3QnRQvm0MHh+bzKC4SIKsFjKSo1mddxCA/9fwO25ml/894oFGbWG16zYmHfg+Z+pd2KyWJgd/+1bUyKEggUFm9EJcZeerkYezs2pjdm90gXws8jMSsx6nNxWX1LpADXuU/2iYzpq8UgAa3ZrvDel9zmYrQ0sboaR2vvORQC/EVTB95TZGpUQzY0yyWUZ51+BevPfFEe761rW8t+uoGXBXbHHwcl6pObOOKXmLhC9/Tyj1fj2X1uBWFqzDHib3+vm8nZWP1QIuN9gsiuy8UmrqXWzaWyEpmQAlgV6Iq2BUSjSL1hUBnoCbnhDJmrxSEqPDWJNXyoTUWJZvLmFdoZPsvFJuTY3lxtcy0LVH6c+ltS7YEzaUyfVPsuT6dP70fhH1jW7C7DYezkhkZe5+qusazZJNCfKBSQK9EFfBjDGelMiidUUMuLYbe46cZnB8BLsOnWRwfAQ5ReUkRIWwcU85U0Yk8G97HiC49uglpWkAvu42lKdinmLJLZ42Cf16hlLX6OaX3xnAjDHJVFbXmb9gpKImcLUq0CulegDPAYPx/Nt6BNgDvAokAvuBH2itj7dqlEIEgOa5+BljkvnH9jKKjpwmISqE3YdOMjwxis/2HychKoTS47WsD/k1/XeWAf4ttAKc6JXBqzcswWrxHOy95JYkcxF1+eYSFnhr5L90nuTNAqccFtIFtHZG/z/A+1rrB5RSdiAMmA/kaK2fUkr9BvgN8EQrn0eITs83kBaWVfHZvkqKjp42g3pidBjb9h9ncFwEu5wnPUFel/nVgOwMdkpHPUVF0r2eBmd1jazOO3hOxYxx+9SZRhZvKGZSehwLJ6WZP8cYmwT6wHLZgV4pFQHcAkwH0FrXA/VKqXuBcd6HvQhsRAK96EJ8Z+7Goqux+WjJ5HQee3E7FgWn61xMSI3lpuui+WDXYQpKq+gVEcx/VcwiNeQQcPHzWgGITKB08M/ZYB/H4z4Hgp8v5+57luzqvINmLx2QippA1ZoZfRJQDqxUSg0B8oGfAb201ocBtNaHlVLXtPTNSqmZwEyAvn37tmIYQlx9vsHdmLnPHpeERXny8CFBFp6ffhO7nVXU1LsAGBwfQUFpFUdO1vGl8yQTUmN5Yv/D9Lcc8nvT0wlrDFE/38UAYMMmByu2OJoE8e6hNlzus2WSzfvVywaorqE1G6ZswI3AUq11OlCNJ03jF631cq31MK31sNjY2FYMQ4ir73ydJncfOonVArUNbv77w70sXFdEkFXRIyyIA5U1jB0Qw27nSbLsi3hu/+30p8yvXLwGDrujmN7zRfO61eL5pTJ7XBLz7hhojsHq8/9y2QDVNbVmRl8GlGmt87z3X8cT6I8qpXp7Z/O9gW9aO0ghOroLdZoEiO1mZ9v+4yigwaVJjA7jq8OnWFvg5B/hf+LGxl3+zeI1lFr7MtH9F7DAsjtTza+53JjNyE6d8eTo509MxeU++/2yAapruuxAr7U+opQqVUoN1FrvASYAX3o/pgFPeT+/1SYjFaKDaV5Fk5Ecw9gBMawtcGK3WcxOk0s+Kqb8dD0WBW7tqZk/UFnDbsuPsAYDrovn4o2KmiIdz101TxES5OaF6Tc1CdBGEDcWWueOTzHLOEXX1tpeN/8fsEYpVQh8G1iEJ8DfrpT6Grjde1+IgOObrgHPDtY3C5yMTomhvtGNy635/OBx3N4o7dbw55AXee2be8h3PYhVeQK8P6ma6oj+fJLpYJL+6wUf29JCqxByOLgQF3G+XjSFZVVmsB87IJY3Cw6ZqRKrBf66fi+1DW4So8M4UFnDX8Je4n7X+/5V0nB2Fl8d0Z/Ce983+88bO1oBlmUOPacfzqUcFC46N38PB5fulUJchO/M/VlvZYtxnJ4nXRPL2oJDZu8ag0UposKCeOPUjykJmcz97ksL8ltcg/hbxja6zdvOOzs9uf5lmUOZd8dAlmUOBTCvgyy0ivOTGb0QfjBmx74z9xljklmxxcGidUWMSolma3El8yd6FkeNkso866N0p/qSWxd8yrf4JON5c9OT8ddDS39VtLTAKroGf2f00utGCD9k+GxEmpQe36SFQPOgf013O/n2x4iy1ACX1oDMpWC49XWWTE5n3kXq3KVaRvhLUjeiy3p2k8NcrDRu+x680fy2sci5aW+5WV1zX3qcma4xzlZ9ry6TKFXj90EgxmeXhgF12cwel9Qk/TJ7XBLLN5e08asXXYnM6EWX5dt7Jq1PpLnYuSxzaJOFzHuf+Zivj57muWnDWL65hPSESNYWOOnVPZhNeytYsLaQTxzHWH/6fp7G5ddxfhpwYeE1buNwxh88i6sWePK7KSzdWMKguEhzQXXpxpImh4EIcakk0Isuy3eTU+q13XG5NVaL4lNHJavzDjJ7XBKFZVWcrm2kpt7FbmcVJ2rq2VHqWdxscLtJT+jBmrxSikKmYtVuvxZbNXDG0p0dU3bwu1WfUbuhmJAgi1kXPyjO8wto6oi+5zQmE+JySOpGdGlG7j3XUYlba267vheLNxQzdkAsSzeWkNYnkuHX9cRuVSxaV8TXR06Z3+tya35ZMp19wZMJ9iPIG60LThDGjik7LjqmxRuKmTqirwR50WoS6EWX5pt7tyjF2oJDDE+M4s2CQ2au/J4hcQQHWVEKqhvO9hN4xfVzUtUhz6aniwV5DScJZ6j1db7K/AKAWVn5BFktzB2fQpDVwqysfHOdQDY9ibYkqRvRZTU/DHtl7n7sNgvb9h9ndEq0mSsvLKsiJTacAm/K5nP7o0SpM4D/rQuO6zBurFvB3PGeTq1/et9zjKCx4WlkcjSzsvJ5bksJO0qrpLukaFNSRy+6rOZ94+N7hPD2zsP07RnGl86TjE+NxaWh9FgNH1Tdi9UnqPuVi9dQp6yk1mYRbLMwtF8UXxzy/LK4O6039wyJO6cufvnmEmbekiT18sIvsjNWBCzfskiDbymkv9/7+Nhks7Kl9FgNa/JKmTshhcMnztA7MoSconL2V1SbQV75fFyIxhvktYXU2ixsFkVdo5teEcHmY5oHefDk5lc9PLzF6xLkRWufs5S8AAAgAElEQVRIoBedTvNmYkYKJq1P5GV/b7/oMMLsVhbnFBMRGsSWM/ezL3gyH52+zwzy/tAaiunDwMaXSa1fTZBV0ejWjE6JZm2Bk4czElmWOVTaEogrSnL0otPxLYv0LUE0gueF0h6FZVXMHpfEnOwCugfb+OZULfPuGMDW4kp+fnt/nnqviB3uH2C5hOAO3ly89rYRrvszQVawWRQNLk+Q31pcyaT0OFbnHWRkcrTM0MUVJTN60Sm1VILoz0w/rU8kSzeWMHZADAeO1XCmwc3T6/diUTDtwxspDpp86UFew3F3KCn12Xy3/r/oExVKg8tTkz8oLoKtxZVMHpHAwGsjzF9QUkkjriQJ9KJTOt8B10YgfXr9HrNapbCsygysRkuBNwucBHlXV880uHl2/+0E+ZmDB09wN+rij+swbqx/HpeGQXERlB0/0yQvP39iKu/tOmou/EpHSXGlSepGdDpPvlHIu4WHzylNvDutN3+8P82c6c8dn2KmcYyg/85OJ28WHCLIqqh3afbaJxOkAO1fLbzR28ClYeZ1H/LZ/uNggYzkSD7bd4xdzpPEdrNTfrqeKSMSSOgZzowxyWaZptGITEolxZUkM3oRUC420y8sq+JMgxurRbE3ZIrfs3itPSdEXVebzfWuV1h5++dUVtcDnlr4OeNTCLFbsVqg/HQ9k9LjzFk8SOWMuLqkjl50Skb+3XcxFrjgCUtPr9/D4g3FbLX/hDjLCcCP5mM+xwCm1GejgSCrIiTI2qQW/tlNDqwWWJxTTFp8JF8dOcXscUm43C0fyC1EW5A6ehHQWlqMXb65pMUWv/+6dhcrtjhYnXeQvJA5xKkT/rUQ1tCg4dvqVZK9QX54YhSNLk2jy92kFt5Y5F2WOZQ1M0ayZHK62StHiKtNAr3olFpK0fSODGFxTnGTqpvFOcWUn65l9If3kO96gF4c8ytNYwZ5/QpVtS4U0Kt7MNv2H+e+9HhsVosc4yc6DUndiE7Bt12BkZIxUiNGWeXscUkszikGmh6g/Y76Bf3cpX5X0zRoGFCfTa+IYI6erCMxOoz9lTWE2a08Nvo6s4WxpGXE1SapGxFQDlRWm90djU1Pi3OKOVBZbc6etxZXMndCCg0uN4s3FPOEewU7+RH99MWDvNG2oEHDUPUq6QmRHD1Zx+iUGCqr6wm2Wejfqxvz7hgoaRnR6Uh5peg0XG7NrKx8eobZOVx1Bpv17Dxlt7OK4zX1PJAzmscsNeBtK+PPviet4RvVk7dv+yeD4iK5e6eTD3YfZcqIBA6dqOXutN68W3iYJ+70HPztm5aRMknRGUigF52G1pq6Rs2BY55Dt93aBWAeyr0zZAbddY3/fWm8n0/bY1k7+gMeH3O2TULztsD3DIlrEtilFl50JpKjF51CrqOCx17cTk29q8n1gdd2Z++RU0wekcAfdo7xawYPnll8kY7nvdFrmXfHwLYfsBBXgOToRcBpaVKy58gpBlzbnfd2HfX/5wB7dB8e7/aMnOAkugRJ3YhO4U/vF+HWns1KDS7NLvs0wlWD54vHoU4FX/gH4AnwOd3u4ddnprEkM51NLWyqEiIQyYxeXHX+HCQSHW6nrtGNzaL4MmQ64aqhyUEgwbrObDLmy7jmVlZe4Q7+X+jjUu8uupxWz+iVUlZgO3BIa323Uuo64BWgJ/A5kKm1rm/t84jAZdTBGwHXaoGlG0vMtga5jgoqq+s9s3iLZxbffMHVuH+CMHrgWaxFw3Edyn8Oeo9NeytYMjmdt1qYtcvCqgh0bZG6+RnwFRDhvf8n4G9a61eUUs8CjwJL2+B5RIDybToWZFEcPVXHgompFJZVsdtZxdPr97Ld+hBhloaLLrbewiqzq2Wuo4JpL2yjocDZpJOlEF1Nq1I3Sqk+wETgOe99BYwHXvc+5EXgvtY8h+gajN41R0/VAfD0+r3sOXKSL957jg/VHMKo96uixgjyhpAgKxnJ0bLoKrq01ubo/xv4NeD23o8GTmitG733y4D4lr5RKTVTKbVdKbW9vLy8lcMQnZ3Ru2ZSuuefy5kGN66df+epoOfoY6m4eAMyoJ5gM8gbi6zLMoeS7W0yJic7ia7qslM3Sqm7gW+01vlKqXHG5RYe2mKhvtZ6ObAcPHX0lzsO0fk1P0jk3/d+nx6NnoDsT+sCgGqCKMz8kgzv/Qs1GZMUjuhqWpOjHwV8Tyn1XSAET47+v4EeSimbd1bfB3Be4GeILsq3SdmXh0+yyT2dqKwaNNDDj9OewLPpqU4FcxNZACzz+VpLzcZk0VV0VZedutFaP6m17qO1TgR+BGzQWk8BPgIe8D5sGvBWq0cpOq3zlU4eqKw2UymvHf8xUarG7BHvVwMyPEE+tXYlD2cksixzqJRICnEe7VFH/wQwTylVjCdn/3w7PIfowMb/ZSML1hYCZ0snH121jfF/2WjmzgE+tP+am7OSCWo86Xd/mnoVzM/qf8K86zeSYV1j9qMHaRksxPm0yc5YrfVGYKP3dgkwvC1+rujYfNMvhlxHBbUNLtbklQKwcFIa6QmR5BSV0yvCbtbLp711J+FnSvzvTQPUhcfx+5oHsA65nzcLnMyfmMqMMcmMTI6W3a1CXIDsjBWXzZit+57oNCe7gIdHJ2K3KtbklZLxxxxyisqxKDh6sp4Pgn5FRlYy3U5+fWlBPqQXGbWLuXvqzxh4bQTzJ6aydGNJk8O/JXUjRMuke6VoFSO4dw+28c2pWp6ffpO5WWnyijzzcd1DbGwIeYKY2n1+94g3HniEKBanvd3kjFbjuQvLqiRlI7os6V4pWsWf/jNwdqPTgWM1nGlws9vpmVX/1/tF5mO22n9CIT8g1o8gb5zXWmvtzrJbP0f9top9mdvpFx1+TlomIzlGgrwQfpBAL1p0vrSM7/F5z25ysGKLwzykOzTIwsJ1RQz6t/coKK3CquDTkDnEqRN+z+Kd9kTS1N8Z7n7efC4J6EK0jgR60SLf/jNPr9/T4mLna9tLWbiuiNnjkggLtnH/jZ5drdUNbt6z/4ri4Mn04tjFyyW9s/hjYUm8M/oNlmUOBeCdnWe3YPj7F4YQ4lwS6MV5GWmZxRuKGTsg5pz8uMHoS2NU2rxv/zWp6pBZF38hWnsOAUlTf+eNjNfN512WOZR+0eHm4/z5C0MI0TIJ9F3YxWbJZ/vPxPFmgZMVW85en5NdwPDrejJlRAJnGtysLXDyUtBC9gVPZqClzO9ZfJGOJyv9ZeZOSGHRuiKM876bp2v8+QtDCNEyOWGqC/PtA29Uyhj3m5+8dENcBIvWFfGl8xSb9pabveJnZeVjUbDKtpAxlt1+ty5w6h6Mqv9fgiyK2eHBLN1YwvyJqbjc5/8+378wpO2wEP6T8souzgjoU0f0ZXXeQTOw+26Gmr5yG6NSovnSeYq1BYeYlB7PDXHdeeHj/Xx45oeeI/2UH2ka72en2xPko8ODqK53UdvgZlJ6HH/7YXqTcTUvnTzfWIXoqvwtr5QZfRd3vlmyb4AdlRLNonVFhARZGBQXwS9330vclyd4zJuE97d9QWVoEk/0WkZOUTkRITYqqxsIsigGxUXwZoGTG+IimDEmuclfE4bmf2HIblgh/CeBvosz8vBzx6ewYss+uofamDGm6Sy6pLyakCALtQ1uXjj2ENeoE2eDu59thFVMKn+LX0FOXikTUmO5JiKENz4/RF2jm28nRHJfetw5qSHfAC5th4W4fBLou7Dms+TuoTYWrfNsdNpaXEl8jxDe23WU7wzqRW7cYnoczQU/WwgbTvTKYELFPJbclc4na3cxITWWgtIqvjMohJUP38S6QiefOI6xcFKamRpqKf8ubYeFuHwS6Duh8zUT86cdgO/3GrNk47rxvU+v/5qh/aJYk1fKlBEJLDz5r+ijuZ7Juz+LrcbDrhtL1LS3WXKB3LrviVCb9pab3ShHJkdLEBeijUh5ZSfUmpryA5XVzMrKJ9dRYQb2WVn5HKis5tlNDgbFRTJjzHV8XFzB9pA5/GHHGPS+TZfWgIxg+G0VTHsbaLoOMHVE33MCuO9fFvPuGCjH/gnRxmRG3wn51pRfagXKPUPieLfwMLOy8nk4I5GVufvN6+AJ+gCF3ebSvfHiu1qhaQOyaoJYmPZP/ujzdd91gJZm65J/F6J9SXllJ2SkXz51VJrVMiOTo/3u5JjrqOCRVZ9R2+AmJMjCCz4dJ8m6l5vZBfi3qxXl6S75y/hX+OrIqXN+4TRfB2h+Xwhx+aS8MoCl9Yk0Z95zx6ewMnc/K3P3mz1i4Px5/OWbSxiVEm1ec7s1u51VFJZV8d2Cx0lgl98NyHYGfZtJp3/NqJRothZXtriIKrN1Ia4+CfQBynfXa2FZFVYLLN1YQrDNwsY95QTbPDXxWRUPEvXPM+b03a9NTxrKoobz7X/5kMlrC1mTV8rolOgW0zJSLSPE1SeLsZ1QYVkVyzKH8nBGIos3FLd4OLZvHn/lx/vMLpOn6xoAqGt0s7riB0SpMyjvrlZ/gnwFPXnuts9J+JcPyXVU8N6uo0wZkYDNapFFVCE6KJnRd1K7nVVNFji7h577VvpWu4Cny2SviBB2uO/DYszg/V1sBepCe/GPm98jLc5T3eNbnmmkYiQtI0THI4G+E7JaYNG6IvNwbGOj0/yJqeZjpq/cZm54SowO4/1T9xOs3HCaS2pboDVscQ9iJv/GCw/eRBqYKaHHx57brkDSMkJ0PBLoOzDfBVXjNnh2rc6fmMrinGI+Kiqn6Mipczo/VtXUs3FPOVNGJPD7nbdiUe5LCu4oQMNWPZjtY14gKHc/s7LyWZY59LJLO4UQV4fk6Dsw341RRqXNrKx8ekeGANDgcpPrqGTqiL4Mimu6WSq1dwQO+2T+sGMMFhovKcifUuHMT9vCDe5XmG35d0YmRzc59eliG6CEEB2LBPoOzHdB9VNHpXm9tsHFwnVFWJQyyytnZeU32Rn7x8IxWCyYC60Xo7VnsfW4DuXVCVvoFx3O89NvMhd5fU99ar4BShZfhejYJHXTgRl94H3bCH9+8DhrC5xYFFgtZ0N4faObP71fxFvd/gz7NuGzWfWitAa3gpTabCaPSCDBzTmnO/l+lnbBQnQuMqPvwEqP1bBwXRErtpQwd3wKyzaX8HFxJTYFbg39eoaxeEMxQ/r0oL7RzR9O/ivs2wT4t6vV+HBrSK7N5r70eN7bdfSCPXMutAFKCNExSQuEDsZ3AXaBdzMSQLjdSnW9C4ApIxI4UlVLTlE5YUFWnuX3jLHuBvxsWwDUaQu3hr7OtRHBFJRWERUWhFKKuwb34tCJWlY9PLy9XqIQoo342wJBZvQdjO8CbELPcCakxgKYQX5CaixuDdv2H0eBGeT92vDknb2nNGTz+bSveWR0IjtKq5iQGsuQhB7MHpdEdl5pkxYJQojO77IDvVIqQSn1kVLqK6XUbqXUz7zXeyqlPlRKfe39HNV2ww0cz25ymIuYxm2jp/ySyenMyspn895ycn0WYQG2fF3BgcoaPnP/iJLgyWaQv5AmKZr6bIKsnrfd5Yb5E1MpKK0iLT7SrwO6hRCdT2tm9I3AL7TW1wMjgZ8qpW4AfgPkaK37Azne+6IZ35n7gcpqHl31WZPKmboGF7mOSs40eKJuQlQoAPUuzQuldxHsrYv3J8hvcQ/iurpskuuzGZ0STZDVYj7XjDHJTUolZ4xJ9qsDphCi87jsqhut9WHgsPf2KaXUV0A8cC8wzvuwF4GNwBOtGmUA8i2d7B0ZwpkGN6HAp45KVmwpod6lsSpwaU9OfmJaHP1eHEacOg5cfGerkYvf4h7E9IYFAFgUJPQM4ye3pjArK593djoBLtgrXgjR+bXJYqxSKhHYDAwGDmqte/h87bjW+oLpm668GPv0+j0s3lCM3arQQIPL836E2a30jgxhXdUkgi3eXIqf57Vq747WqfXzzWuJ0WHsr6whLjKE3CcnkOuo4J2dTj7YfVR6xQvRSV2xxVilVDfgH8C/aK1PXsL3zVRKbVdKbS8vL2/tMDol341HNqvFDPIAP7+9PzmnHyDY4jYXWi86i+dsquYR1wLz+qC4CCqr67FZvG2G8fxF0S86XEolhegCWrVhSikVhCfIr9Fav+G9fFQp1VtrfVgp1Rv4pqXv1VovB5aDZ0bfmnF0ZOc7AMR3Ng2wYkuJ+fX7bVuZmDMXTcMlndVaj5Vh6mX6xYZR7zyJ3WbBqqBHaBAHgVC7jb/+YIj5PdIrXoiuoTVVNwp4HvhKa/20z5feBqZ5b08D3rr84XV+vouuz25ysGKLgznZBQBmkP/F33ficmtCgyz86tqdLLStII4K/1sXaGjAysDaLIb0iWS38ySD4iIItlm4c/C1bHVUttizXgjRNbRmRj8KyAS+UErt8F6bDzwF/F0p9ShwEHiwdUPsHM43czfKJedkFzB2QCxvFhwy2wsbOfF+PUN5/cwjxFlOoE74/5xawzeqJ7e6l1JT52Lgtd34uLiSKSMSWDgpjRVbHCxaV8Sk9DhzoVUqaoToelpTdfMx56/um3C5P7ez8j26r6WFTaOEcVJ6PEs3lrD6k4N8c6qW56ffxOBXRtLdcsLvGbzRQvi0PRbHjz7FmpWP3WZhz5HTjE6J9vSgj3E0qYt/cFiCLLQK0UVJC4Q2ZAT35n3am18fOyCGtQVOdtmnEW7xLw9vvE0NysqA2ixGp8Sw+rERPLvJgdXiOT3qmu4hnKprZPa4JLYWVzLzlqQW/8KQWb0QgcHfqhvpXtmGfGfuc8entDizN06DKgqZTrD2L8ifwc6GAf/KL4sGUNvgZnRKNFuLK1ixxWH2qbdZLfzx+98COO/MXRZaheiaJNC3EWNm3fwc163FlU1m9vs2rKKwx2sE19b7VS55mBhOj5pPVNK92L7OJwTPpqf5E2NZtK6IG+K6A7Asc6gZxOXcViGELwn0l8joET9jzNn0x4otDl7bXkpJeXWL57gaAbdm+8v8p2UF1tozF30eDVSqaPZPzSMjOYYNmxzmKU+FZVXMGJPMl86TrC1wmn89GGTmLoTwJYH+Eo1KiWbRuiIAZoxJNitbbk2N5UfDE1i6sYSPisr54lDV2QZhS0agK4qYgB+9abyPqQvpxes3v8fj3oDd/CCQXEcFm/ZWSOsCIcRFSaD3g2/ppDGTX7iuiJdyD1B2/Iw5iwc4dabRbGkwKC6SjPcmoiuK/F5wPaPs7Mj8ypNnP88BIM3z/nLKkxDiQqQfvR+ab3oCsFkUpcfPMODabgyKizRbDa/M3c+guAg+ss7m5peS/QryxqanahXEsxkfXzRoyylPQohLIeWVfjAWWpduLGHsgFjWFhwCILabnfLT9ditil/dOZCxOd+jP2Xm9/kzi6/Rdn7T8Bhvu0czOiWaj4srmTs+hXl3DGynVyOECBRywlQbSusTeU6QBxjdPxa7VVHv0tyacy/9KTvbgOwiP1MDZe4Y/l3PJHHcdOxWxcfFlSRGh7E676B5KIkQQrSWBHo/FJZVcdfgXrxZcIjIEM+yxuC4CNYWHOKjsN+wL2QyybrU7wZkACUkMLp+MQNvf4SRydHYvKc+WS3KbJkgwV4I0RZkMfY8fBdgrRbIzitlUFwEu5wnGez9vCH0CeLqSz318P70ifd+PhaaxH9es4wFKdEs3VjC9dd2x2pRLPBW6fjm3GVxVQjRWl0i0F+o4Zhv2aLv44wF2Nnjkng5r5RvJ0RSUFpFZIiNlyoeJCrkjN8HgYBnsbVC9eTNCf/01NdneGrxjSqdueNTmtTmSy28EKKtdInUjW/VDJwtT0xrVr7o+7jlm0tIT4hk0boiwoKtFJRW0SsimI/c04hSZ/zOwxuHgTh1DxZdv7ZJozHfg0ckLy+EaC8BW3XTfBaf66hgVlY+34qPpOjIqfOWLxq/BG7oHcHHxRUMjo9g16GTfBLyU67Vx8GfA7m9/7NH9+HO+j8TEmRhWL+oJhU1zWvh5Rg/IcSl6vJVN81n8QANLje5jkqmjuh73mBqNCb7uLjCk4v3CfLKnyCvPTn4G9yvcGf9n73Pq/m4uJJJ6fGszjvIii0Olm8ukVp4IcQVEbA5eiNwGu2BV+buJ8hqYeaYJFZs2Uf3UFuTnLiRrhmVEs3qvINMSo/j33bf5Xcu3ugTXx3Zn78kvoDa4QQgMsRGVW0jQVbFg8P6cENc93N64PiOWWbzQoi2FrCBHpq2DbbbLKx6+CYykmPY5axi4boiPnFU8sL04WZap3uwjU17ypk/MZUf5oyhu8WTi7/YNF5rOKnCGc1K5t6UwpeFh7FaFKNTYs7+ZeA8ycJ1X3K4qu5sDxwhhLgCAjZ1A2cXOwfFRVDf6Ga305MWuTk5GoAtX1fw9Po9zMrKByC1d3e+sE/jsZwb6U61f4utGo7rUKbH/p1Gl5tF64qIDrfzvSG92VpcwaT0eJxVtYxOiWG38xRTR/RlxphkOfxDCHHFBOyMvvniptFl8kvnSTbtrWDBxFT+un4vizcUs9q+iFGWXbAfsPjXugDgVFAsr97yged0p+oGbFYLIcDRk7V8VFRuNjs7e3ZrvHSaFEJccQEb6Js3/mrev31QnKe08qWghYxSuy9pVytAbUgvsm9+j8eb1cID3rNh48wDwJue3dpHqmuEEFdUwAb65qkR3/7tz24qYebHo/jK2gD4P4PXgAqOJPcHn5tthH1r4Vfm7gdoUhff/BcOyAlQQogrK2ADva/maZxZuaMJ8/O8Vjh7MPdxHcp/Jr3FJu/PgrPnswJmoB+ZHH3BHvFSXSOEuJI6/WKs0QfeV66jgukrt5nXC8uq2Bz+JDdnJaN/G0kYFz+v1WAcBvLJQw5GuF5gbYHTrMP3na0XllWxLHMoyzKHmrN1qYsXQnQEnX5Gb2yMar7DdPa4JPP6419MRp/8+tJm8ArQUK2DePm2TxkEhARZuSkx0lxQ9U0PNT/qz/gsM3chxNUWEC0QjOA+dURfVucdNIN+7VMDCK49CviXhzf+S2xxDeKhhgVYFDz53VRKyqv5YPdRZo9LwuU+95eLEEJcDQHdAqF5uiYjOYaxA2JYvKH4bHuDv6QSUnvUr+Zj4AnyLhXCcxM+56GGBQC4NeyvqKZfdDizxyWxdGOJ2T9H0jJCiM6iUwb65n1sVmxx8GaBk0FxEfTO/Vfcv+uJPn34oj9H+3xUu4NI1y+xcF0RAJPS47BbFWvySvn463KWbjy3N41sehJCdAadMkdfWFZl5uDHDojlzYJDTB6RwMTSv3Iz61F+ZKO0hmNhSUQ/UcCCtYWsySvFohoBWODd6PTgsAQeej7P7DopaRohRGfULoFeKXUn8D+AFXhOa/1UW/7893Yd5uujp/nOoGtZW3CI5T2zGb/j/7Aqt38thPG0EL7r+B+46dlcPtt/HJsFGt0wKT2+SbOzULuNb8VHyo5WIUSn1eapG6WUFXgGuAu4AfixUuqGtnyOu9N6U1PvYm3BIZb2WMPt1e9i8zPIq269+STTwYOWp1EKtu33tB8OtduYOz6FTXvLyXVUmAu8yzKHkj1jpJzjKoTotNpjRj8cKNZalwAopV4B7gW+bKsnGBQXSYH9MXqoGjjjRwth7+e6kF6E/LKIDOB7Q3qzJq8U8Cy6fm9Ib+bdMdDc6PSdQb3O2y9eZvVCiM6kPQJ9PFDqc78MGNGWTzA4K43ulhr/qmk0/F/Id3GO/oNnQdVRwW5nFWvySrFZFCOu68ln+4+RnVdKYkw4M8YknzegS128EKIzao+qm5bi7znLo0qpmUqp7Uqp7eXl5Zf0BP62EHZj4RV1B//o/XOWbixh9rgkCsuqeGWb5/fQE3cNZM2Mkax6ZDghQRbeLfRU6khFjRAikLTHjL4MSPC53wdwNn+Q1no5sBw8G6bacgAa+DD0bn5x5iGWZQ7lBe+O2VlZ+aTFR+I8UWtW1oAnsD8//SapixdCBKT2CPSfAf2VUtcBh4AfAZPb4XnOoQGlrOy45j5mHvg+dlvTY5zqGt1sdXhKJX0ra0DSMkKIwNXmqRutdSMwB/gA+Ar4u9Z6d1s+hwqOPCcXZLYQnrqXRyt+zKT0OOob3Tz24naeXr+Hx17cTn2j2zz8Q6pnhBBdRafsdfPkG4X8uvA79KDGvHaCMH6R+BY7SqvMnjRWC+ZOVzi7Eap522IhhOiMArrXDcAtrOKTTAefZDpI4+9kuF6gsrq+SU+aQXGR2G2el2i3WcxTpaRXjRCiK+mUgf6P96exLHMoc7IL+NRRCYDNamFs/1izJw3ArKx8gm0W5o5PIdhmYVZWvpmykcoaIURX0SkDPXgC9dQRfVm8oZiHMxJ5OCOxSffKd3Z6Cn2WZQ5l3h0DWZY5FMC8LoQQXUWnbGoGXPCs1pHJ0fSLDmdZ5tAmO1uN05+EEKIr6ZQzet/F1JHJ0eb1kcnRZk8ao2+8L0nXCCG6ok4Z6OWsViGE8F+nLK8UQgjRBcorhRBC+EcCvRBCBDgJ9EIIEeAk0AshRICTQC+EEAGuQ1TdKKXKgQOX+e0xQFdrRSmvuWuQ19w1tOY199Nax17sQR0i0LeGUmq7P+VFgURec9cgr7lruBKvWVI3QggR4CTQCyFEgAuEQL/8ag/gKpDX3DXIa+4a2v01d/ocvRBCiAsLhBm9EEKIC+jUgV4pdadSao9Sqlgp9ZurPZ72oJRKUEp9pJT6Sim1Wyn1M+/1nkqpD5VSX3s/R13tsbYlpZRVKVWglHrXe/86pVSe9/W+qpSyX+0xtiWlVA+l1OtKqSLve31zF3iPf+79N71LKfWyUiok0N5npdQLSqlvlFK7fK61+L4qj8XeeFaolLqxrcbRaQO9UsoKPAPcBdwA/FgpdcPVHVW7aAR+obW+HhgJ/NT7On8D5Git+wM53vuB5GfAVz73/wT8zft6jwOPXpVRtZ//Ad7XWqcCQ/C89oB9j5VS8cBcYJjWejBgBX5E4L3Pq4A7m1073/t6F9Df+zETWMLIoIIAAAKzSURBVNpWg+i0gR4YDhRrrUu01vXAK8C9V3lMbU5rfVhr/bn39ik8ASAez2t90fuwF4H7rs4I255Sqg8wEXjOe18B44HXvQ8JtNcbAdwCPA+gta7XWp8ggN9jLxsQqpSyAWHAYQLsfdZabwaONbt8vvf1XuAl7fEp0EMp1bstxtGZA308UOpzv8x7LWAppRKBdCAP6KW1PgyeXwbANVdvZG3uv4FfA27v/WjghNa60Xs/0N7rJKAcWOlNVz2nlAongN9jrfUh4C/AQTwBvgrIJ7DfZ8P53td2i2mdOdCrFq4FbAmRUqob8A/gX7TWJ6/2eNqLUupu4Butdb7v5RYeGkjvtQ24EViqtU4HqgmgNE1LvHnpe4HrgDggHE/qorlAep8vpt3+nXfmQF8GJPjc7wM4r9JY2pVSKghPkF+jtX7De/mo8Wed9/M3V2t8bWwU8D2l1H486bjxeGb4Pbx/4kPgvddlQJnWOs97/3U8gT9Q32OA24B9WutyrXUD8AaQQWC/z4bzva/tFtM6c6D/DOjvXaW341nIefsqj6nNefPTzwNfaa2f9vnS28A07+1pwFtXemztQWv9pNa6j9Y6Ec97ukFrPQX4CHjA+7CAeb0AWusjQKlSaqD30gTgSwL0PfY6CIxUSoV5/40brzlg32cf53tf3wYe8lbfjASqjBRPq2mtO+0H8F1gL+AAFlzt8bTTaxyN58+3QmCH9+O7ePLWOcDX3s89r/ZY2+G1jwPe9d5OArYBxcBrQPDVHl8bv9ZvA9u97/ObQFSgv8fA74AiYBeQBQQH2vsMvIxnDaIBz4z90fO9r3hSN89449kXeCqS2mQcsjNWCCECXGdO3QghhPCDBHohhAhwEuiFECLASaAXQogAJ4FeCCECnAR6IYQIcBLohRAiwEmgF0KIAPf/A4DPU0EUbd9uAAAAAElFTkSuQmCC
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 15, Loss = 4.00606113481368
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 16, Loss = 3.9558877693135264
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 17, Loss = 3.933123951630546
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 18, Loss = 3.9227958761575064
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 19, Loss = 3.918109910704811
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Iteration = 20, Loss = 3.9159837768231243
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Make-Predictions-for-Valid-Dataset">Make Predictions for Valid Dataset<a class="anchor-link" href="#Make-Predictions-for-Valid-Dataset">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">valid_predictions</span> <span class="o">=</span> <span class="n">valid_dataset</span> <span class="o">*</span> <span class="n">parameters</span><span class="p">[</span><span class="s2">&quot;w&quot;</span><span class="p">]</span> <span class="o">+</span> <span class="n">parameters</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">valid_dataset</span><span class="p">,</span> <span class="n">valid_labels</span><span class="p">,</span> <span class="s1">&#39;x&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">valid_dataset</span><span class="p">,</span> <span class="n">valid_predictions</span><span class="p">,</span> <span class="s1">&#39;o&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#cost for valid dataset</span>
<span class="n">cost_function</span><span class="p">(</span><span class="n">valid_predictions</span><span class="p">,</span> <span class="n">valid_labels</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt output_prompt">Out[13]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>4.051810568090534</pre>
</div>

</div>

</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
