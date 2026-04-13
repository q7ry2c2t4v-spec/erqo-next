# iMessage対応アプリとステッカー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/imessage-apps-and-stickers

# iMessage対応アプリとステッカー

iMessage対応アプリを使えば、ほかのユーザとのやりとりで、コンテンツを共有したり、共同作業したり、ゲームをプレイしたりすることができます。ステッカーは、会話を盛り上げるのに役立ちます。

![iMessageアプリアイコンのスケッチ。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/e073f325aa95fa10c5f7bd4e00bc8378/technologies-iMessage-Apps-intro%402x.png)

iMessage対応アプリやステッカーパックは「メッセージ」での会話のやりとりで使用でき、またエフェクトとしても「メッセージ」およびFaceTimeで利用できます。iMessage対応アプリとステッカーパックは、スタンドアロンアプリや、iOSまたはiPadOSアプリ内のアプリ機能拡張として作成できます。デベロッパ向けのガイダンスは、[Messages](/documentation/Messages)および[ステッカーパックとiMessageアプリをシステムのステッカーアプリ、メッセージのカメラ、およびFaceTimeに追加する](/documentation/Messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Best-practices)

**iMessage対応アプリでは主要な体験を1つに絞って提供する。** ユーザがiMessage対応アプリを選択するのは会話のやり取りの中なので、アプリの機能やコンテンツは分かりやすく、かつすぐに利用できる必要があります。提供したい機能やコンテンツが複数ある場合は、その1つ1つに個別のiMessage対応アプリを作成することをおすすめします。

**iOSやiPadOSアプリ内のコンテンツの提供を検討する。** 例えばiMessage対応アプリからショッピングリストや旅行プランなど、ユーザが共有したいと思えるようなアプリ独自の情報を提供したり、食事をする店や見る映画を決めるなど、シンプルな共同作業を行ったり、といったことが考えられるでしょう。

**コンパクトビューには最も重要な機能を提示する。** ユーザは、メッセージのやり取りの下に表示されるコンパクトビューでiMessage対応アプリを操作できます。このビューはウインドウのほぼ全体にまで拡大できます。使用頻度の高い項目をコンパクトビューに表示するようにし、それ以外のコンテンツは拡大ビューに表示するようにしましょう。

**テキスト編集は基本的に拡大ビューでのみ有効にする。** コンパクトビューはキーボードとほぼ同じスペースを占有します。iMessage対応アプリのコンテンツが編集作業中も見えるようにするには、キーボードを拡大ビューに表示する必要があります。

**表現力があり、インクルーシブで、用途の広いステッカーを作成する。** ステッカーは表現力豊かな静止画像にすることも短いアニメーションにすることもできます。いずれにしても、さまざまな背景に配置したときや、回転したり拡大/縮小したりしたときに可読性が失われないようにしてください。テキスト、写真、他のステッカーと視覚的に統合しやすいステッカーにするために、透過処理を利用することもできます。

**ステッカーごとに、ローカライズされた代替となる説明を付ける。** VoiceOverでステッカーの説明を読み上げられるようにして、ステッカーパックの利用をサポートします。

## [仕様](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Specifications)

### [アイコンのサイズ](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Icon-sizes)

iMessage対応アプリまたはステッカーパックのアイコンを「メッセージ」、App Store、通知、「設定」に表示できます。ユーザがiMessage対応アプリやステッカーパックをインストールすると、そのアイコンがメッセージアプリのアプリパネルにも表示されます。

各機能拡張にそれぞれ四角いアイコンを提供してください。角を丸めるマスクがシステムから自動的に適用されます。

状況を問わず、さまざまなデバイスでアイコンの優れた見た目を保証するには、角のある四角いアイコンを以下のサイズで作成します:

使用目的| @2x（ピクセル）| @3x（ピクセル）  
---|---|---  
「メッセージ」、通知| 148x110| -  
| 143x100| -  
| 120x90| 180x135  
| 64x48| 96x72  
| 54x40| 81x60  
「設定」| 58x58| 87x87  
App Store| 1024x1024| 1024x1024  
  
### [ステッカーのサイズ](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Sticker-sizes)

「メッセージ」は小型、標準、大型のステッカーに対応します。コンテンツに最適なサイズを選び、そのサイズですべてのステッカーを準備してください。1つのステッカーパックは同じサイズで統一してください。「メッセージ」はステッカーを格子状に整頓し表示します。異なるサイズごとに表示方法が変わります。

![iPhone画面の下半分を示した図。小型のステッカーがグリッドで表示されています。表示されているステッカーが8枚、それに続く4枚のステッカーが一部見えていて、3列に配置されています。](https://docs-assets.developer.apple.com/published/a64edfeafbb874560b2a72b04505ff43/sticker-sizes-small%402x.png)

小型

![iPhone画面の下半分を示した図。標準のステッカーがグリッドで表示されています。6枚のステッカーが2行×3列に配置されています。](https://docs-assets.developer.apple.com/published/092a81eb61dbb7310098aecf4c0c73a7/sticker-sizes-regular%402x.png)

標準

![iPhone画面の下半分を示した図。大型のステッカーがグリッドで表示されています。完全に表示されているステッカーが2枚、それ続く2枚のステッカーが一部見えています。](https://docs-assets.developer.apple.com/published/7d0d3ead02ab892c2eaa8c575707c3d5/sticker-sizes-large%402x.png)

大型

選択したステッカーサイズに合わせて、以下の@3x寸法でステッカー画像を作成してください。システムは必要に合わせて実行時に画像をダウンスケーリングし、@2xおよび@1xバージョンを生成します。デベロッパ向けのガイダンスは、[`MSStickerSize`](/documentation/Messages/MSStickerSize)を参照してください。

ステッカーのサイズ| @3x寸法（ピクセル）  
---|---  
小型| 300x300  
標準| 408x408  
大型| 618x618  
  
ステッカーファイルのサイズは500 KB以下にする必要があります。次の表に、透過処理およびアニメーションを利用する場合の対応フォーマットごとのガイドを示します。

フォーマット| 透過処理| アニメーション  
---|---|---  
PNG| 8ビット| ×  
APNG| 8ビット| 〇  
GIF| 単色| 〇  
JPEG| ×| ×  
  
## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Platform-considerations)

 _iOS、iPadOSに追加の考慮事項はありません。macOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Related)

[iMessage対応アプリとステッカー](https://developer.apple.com/imessage/)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Developer-documentation)

[Messages](/documentation/Messages)

[ステッカーパックとiMessageアプリをシステムのステッカーアプリ、メッセージのカメラ、およびFaceTimeに追加する](/documentation/Messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime) — メッセージ

#### [ビデオ](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Videos)

[](https://developer.apple.com/videos/play/wwdc2017/820)

## [変更履歴](/jp/design/human-interface-guidelines/imessage-apps-and-stickers#Change-log)

日付| 変更内容  
---|---  
2023年5月02日| ガイダンスを1ページに統合しました。
