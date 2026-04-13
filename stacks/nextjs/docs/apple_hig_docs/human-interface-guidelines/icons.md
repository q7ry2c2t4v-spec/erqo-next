# アイコン

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/icons

# アイコン

効果的なアイコンとは、ユーザがすぐに理解できる形で特定の概念を表現するグラフィックアセットです。

![Commandキーのアイコンのスケッチ。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる黄色になっています](https://docs-assets.developer.apple.com/published/8f312fec90e1ce0daa2692f18d877882/foundations-icons-intro%402x.png)

アプリやゲームでは、選択可能な項目やアクション、モードを分かりやすい形でユーザに伝えるために、シンプルなアイコンが数多く使用されています。[アプリアイコン](/jp/design/human-interface-guidelines/app-icons)では、シェーディング、テクスチャ、ハイライトなどの高度な視覚効果を使用してアプリの個性を伝えることができます。それとは違い、 _インターフェイスアイコン_ では、シンプルな図形や限られたカラーを使用して明確なアイデアを示すことが一般的です。

インターフェイスアイコン（ _グリフ_ とも呼ばれます）は、自分でデザインすることも、SF Symbolsアプリのシンボルから選んでそのまま使用することも、ニーズに合わせてカスタマイズすることもできます。インターフェイスアイコンとシンボルは、どちらも黒と透明で形状を定義しています。画像の黒い部分にはシステムで別のカラーを適用することもできます。ガイダンスは、[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/icons#Best-practices)

**認識しやすいシンプルなデザインを作成する。** 細かすぎるインターフェイスアイコンは分かりにくく、判別しにくくなります。ほとんどのユーザがすぐに認識できるシンプルで普遍的なデザインにしてください。通常、開始するアクションや対応するコンテンツに直接関係する見慣れたものを視覚的に表現すると効果的なアイコンになります。

**アプリのすべてのインターフェイスアイコンで視覚的な一貫性を維持する。** カスタムのアイコンのみを使用する場合でも、システムが提供するアイコンと組み合わせる場合でも、アプリのすべてのインターフェイスアイコンで、サイズ、細かさのレベル、線の太さ、視点を統一する必要があります。アイコンの視覚的な重みによっては、ほかのアイコンとの視覚的な一貫性が保たれるように、大きさを調整する必要がある場合もあります。

![横に並んだ4つのグリフの図。左から、カメラ、ハート、封筒、目覚まし時計のグリフが示されています。2つの水平な点線は上下の境界を、赤い水平線は中央を示しています。4つのグリフはすべて黒で塗りつぶされており、内側に白い線で詳細が描かれているものもあります。目覚まし時計の上部は、一部が上の点線からはみ出しています。これは視覚的な重みが軽い分を高さで補って、ほかのグリフとのバランスを取るためです。](https://docs-assets.developer.apple.com/published/f1cf8ce0ca53b7cb3bce1391a378f6ce/custom-icon-sizes%402x.png)視覚的な一貫性を保つため、必要に応じて個々のアイコンの大きさを調整し…

![上と同じ4つのグリフ、上下の水平な点線、中央の赤い水平線を示した図。この図では、すべての線が同じ太さであることを強調するため、4つのグリフすべてが灰色で塗りつぶされており、内側の線は黒になっています。](https://docs-assets.developer.apple.com/published/91320cdd7a31574df355383d83eb1ceb/custom-icon-line-weights%402x.png)…すべてのアイコンで同じ太さの線を使用しています。

**通常はインターフェイスアイコンの太さを周囲のテキストと合わせる。** アイコンかテキストを強調したい場合以外は、両方を同じ太さにすることで、コンテンツの見た目と強調レベルをそろえます。

**視覚的な位置合わせのために必要に応じてカスタムインターフェイスアイコンにパディングを追加する。** 非対称なアイコンなど、一部のアイコンは、見た目ではなく幾何学的に中央に配置すると、バランスが崩れて見える場合があります。例えば、下のダウンロードアイコンの場合、幾何学的に中央に配置すると、視覚的な重心が下に来るので、下が狭く見えます。

![黒い円の中に、白い水平線を指す下向きの白い矢印がある2つの画像。右側の画像には2つの水平なピンク色のバーがあり、1つは円の上とグリフの上端の間、もう1つはグリフの下端と円の下の間に配置されています。これにより、グリフは幾何学的に円の中心にあることを示しています。](https://docs-assets.developer.apple.com/published/1c13eed753a1ebcfd6d35929738476c7/asymmetric-glyph%402x.png)非対称なアイコンは、中央に配置されていてもそうでないように見えます。

このような場合は、アイコンの位置をわずかに調整し、見た目が中央になるようにします。インターフェイスアイコンの周囲に調整用のパディングを設けてアセットを作成した場合は（下の図の右側）、アセットを幾何学的に中央に配置すればアイコンの見た目も中央になります。

![黒い円の中に、白い水平線を指す下向きの白い矢印がある2つの画像。左側の画像には2つの水平なピンク色のバーがあり、さきほどの図と同じように配置されていますが、グリフは数ピクセル上に移動しています。右側の画像では、パディング領域を示すピンク色の長方形がグリフの上に重ねられています。パディング領域には、グリフの下の数ピクセルも含まれています。](https://docs-assets.developer.apple.com/published/c31bce31456820badff997c95db264c6/asymmetric-glyph-optically-centered%402x.png)アイコンを数ピクセル上に動かすことで、見た目が中央になります。この数ピクセルをパディングに含めれば、簡単に中央に揃えることができます。

見た目を中央にするための調整はほんの数ピクセルだけですが、アプリの見た目に大きな影響を与える可能性があります。

![黒い円の中に、白い水平線を指す下向きの白い矢印がある2つの画像。左側のグリフは幾何学的な中央、右側は視覚的な中央に配置されています。](https://docs-assets.developer.apple.com/published/5d9da37476ee3225a29ce3efbfd86cac/asymmetric-glyph-before-and-after%402x.png)視覚的な中央に合わせる前（左）と後（右）。

**選択状態のバージョンのインターフェイスアイコンは必要な場合のみ準備する。** タブバー、ボタンなどの標準的なシステムコンポーネントで使用されるアイコンについては、選択された状態と選択されていない状態の見た目を準備する必要はありません。選択された状態の見た目は、システムによって自動的に更新されます。

![背景を共有する2つのツールバーボタンの画像。左側のボタンは、選択された状態のフィルタアイコンを表し、背景に青の色合いが使用されています。右側のボタンは、選択されていない状態のその他アイコンを表し、ツールバーボタンのデフォルトの見た目が使用されています。](https://docs-assets.developer.apple.com/published/b5c874fca24c428b421c008b29709986/icons-selection-correct%402x.png)ツールバーでは、選択された状態のアイコンにはアプリのアクセントカラーが適用されます。

**インクルーシブな画像を使用する。** 誰もが理解しやすく、歓迎されるようなアイコンになるように考慮します。人物をデザインする際は性別によらない表現にするようにします。文化や言語が異なると認識しにくいおそれのある画像を使用しないでください。ガイダンスは、[インクルージョン](/jp/design/human-interface-guidelines/inclusion)を参照してください。

**意味を伝えるためにどうしても必要な場合を除きデザインに文字を含めない。** 例えば、テキストの形式を示すインターフェイスアイコンに文字を使用するのは、その概念を最も直接的に伝える方法です。アイコンに個々の文字を表示する必要がある場合は、文字をローカライズするようにしてください。テキストの連なりを表現する必要がある場合は、抽象的なデザインにし、右から左に書く場合に使用できるように反転したバージョンも含めてください。ガイダンスは、[右から左](/jp/design/human-interface-guidelines/right-to-left)を参照してください。

![大文字のAのように見える文字シンボルの情報パネルを表示したSF Symbolsアプリのスクリーンショットの一部。その画像の下には、ローカライズされたバージョンの8つのシンボル（ラテン文字、アラビア文字、ヘブライ文字、ヒンディー文字、日本文字、ハングル文字、タイ文字、漢字）が表示されています。](https://docs-assets.developer.apple.com/published/8555103b5ad7fdf48c0234a869f0af33/character-in-glyph%402x.png)個々の文字を表示するアイコンのローカライズ版を作成します。

![SF Symbolsアプリのスクリーンショットの一部。テキストドットページのシンボルの情報パネルが表示されています。角丸四角形の中に左揃えの3本の水平線が並んでいるように見えます。その画像の下には、左から右と右から左それぞれの書字方向用のローカライズ版が表示されています。](https://docs-assets.developer.apple.com/published/a822c7609dfeec9d9661841d7e74e502/abstract-text-in-glyph%402x.png)読む方向を示す反転版のアイコンを作成します。

**カスタムのインターフェイスアイコンを作成する場合は、PDFやSVGなどのベクターフォーマットを使用する。** ベクターベースのインターフェイスアイコンは、高解像度ディスプレイで自動的に拡大されるので、高解像度版を提供する必要はありません。逆に、アプリのアイコンなどの画像に使用するPNGには、シェーディング、テクスチャ、ハイライトなどの効果が含まれるので、拡大に対応していません。そのため、PNGベースのインターフェイスアイコンでは、それぞれについて複数のバージョンを提供する必要があります。または、カスタムのSF Symbolを作成し、シンボルの強調度合いが周囲のテキストと一致するように倍率を指定することもできます。ガイダンスは、[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)を参照してください。

**カスタムのインターフェイスアイコンに代替テキストラベルを指定する。** 代替テキストラベル（アクセシビリティ説明）は画面には表示されませんが、画面にあるものをVoiceOverの音声で説明するために使用されます。これは、視覚障がいのあるユーザが要素間を移動する助けになります。ガイダンスは、[VoiceOver](/jp/design/human-interface-guidelines/voiceover)を参照してください。

**Appleハードウェア製品のレプリカを使用しない。** ハードウェアのデザインは頻繁に変更されるため、インターフェイスアイコンなどのコンテンツが古くさく見える可能性があります。Appleのハードウェアを表示しなければならない場合は、[Appleデザインリソース](https://developer.apple.com/design/resources/)か、さまざまなApple製品を表すSF Symbolsで利用できる画像のみを使用するようにします。

## [標準のアイコン](/jp/design/human-interface-guidelines/icons#Standard-icons)

Appleプラットフォームのインターフェイスにおける[メニュー](/jp/design/human-interface-guidelines/menus)、[ツールバー](/jp/design/human-interface-guidelines/toolbars)、[ボタン](/jp/design/human-interface-guidelines/buttons)、およびその他の場所で一般的なアクションを表すアイコンには、これらの[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)を使用できます。

### [編集](/jp/design/human-interface-guidelines/icons#Editing)

アクション| アイコン| シンボル名  
---|---|---  
カット| ![ハサミを表すアイコン。](https://docs-assets.developer.apple.com/published/16c5fe84ae743e06cf2d388fc64e0cf4/icons-symbols-meaning-cut%402x.png)| `scissors`  
コピー| ![2部の書類を表すアイコン。](https://docs-assets.developer.apple.com/published/a88919c55265efbadeac0df5e16ffd05/icons-symbols-meaning-copy%402x.png)| `document.on.document`  
ペースト| ![クリップボードの前面にある書類を表すアイコン。](https://docs-assets.developer.apple.com/published/20e32bbb2a3a94eb35d01ddfa9c630e0/icons-symbols-meaning-paste%402x.png)| `document.on.clipboard`  
完了| ![チェックマークを表すアイコン。](https://docs-assets.developer.apple.com/published/833bd3b8ccdf0e2fee0893b3858ddae5/icons-symbols-meaning-done-save%402x.png)| `checkmark `  
保存  
キャンセル| ![Xを表すアイコン。](https://docs-assets.developer.apple.com/published/b834206c8d155bc1b0d9d17c206c6da3/icons-symbols-meaning-close-cancel%402x.png)| `xmark`  
閉じる  
削除| ![ゴミ箱を表すアイコン。](https://docs-assets.developer.apple.com/published/61f8368d02b05af22d3253a892ced7f3/icons-symbols-meaning-delete%402x.png)| `trash`  
取り消す| ![左上に向かって湾曲した矢印を表すアイコン。](https://docs-assets.developer.apple.com/published/e3e973d07e4cfa983c92e37da5b3e104/icons-symbols-meaning-undo%402x.png)| `arrow.uturn.backward`  
やり直す| ![右上に向かって湾曲した矢印を表すアイコン。](https://docs-assets.developer.apple.com/published/0f263db97ca2b7c31bbbd3cd5682d071/icons-symbols-meaning-redo%402x.png)| `arrow.uturn.forward`  
作成| ![正方形の上に置かれた鉛筆を表すアイコン。](https://docs-assets.developer.apple.com/published/cfac914468b7fa2f287495f8644f3937/icons-symbols-meaning-compose%402x.png)| `square.and.pencil`  
複製| ![別の正方形に重なっている、プラス記号が付いた正方形を表すアイコン。](https://docs-assets.developer.apple.com/published/96323f746d3c67172648745420a15c27/icons-symbols-meaning-duplicate%402x.png)| `plus.square.on.square`  
名称変更| ![鉛筆を表すアイコン。](https://docs-assets.developer.apple.com/published/8d3692b6e29cf0cdcb7885af414b2693/icons-symbols-meaning-rename%402x.png)| `pencil`  
移動| ![フォルダを表すアイコン。](https://docs-assets.developer.apple.com/published/77c3e45c395bf2d2225c85979eca53a8/icons-symbols-meaning-move-to-folder%402x.png)| `folder`  
フォルダ  
添付| ![クリップを表すアイコン。](https://docs-assets.developer.apple.com/published/e493eab83f8cc2a6f0aaa2ced386dcff/icons-symbols-meaning-attach%402x.png)| `paperclip`  
追加| ![プラス記号を表すアイコン。](https://docs-assets.developer.apple.com/published/e0a7d36fc7aecfd6e49a4d0c0cb196af/icons-symbols-meaning-add%402x.png)| `plus`  
その他| ![省略記号を表すアイコン。](https://docs-assets.developer.apple.com/published/92e0b17a3881b62008563deb4a2aca40/icons-symbols-meaning-more%402x.png)| `ellipsis`  
  
### [選択](/jp/design/human-interface-guidelines/icons#Selection)

アクション| アイコン| シンボル名  
---|---|---  
選択| ![円の中にあるチェックマークを表すアイコン。](https://docs-assets.developer.apple.com/published/7eac493b5a3896062a90328117d43e90/icons-symbols-meaning-select-all%402x.png)| `checkmark.circle`  
選択解除| ![Xを表すアイコン。](https://docs-assets.developer.apple.com/published/b834206c8d155bc1b0d9d17c206c6da3/icons-symbols-meaning-deselect-close%402x.png)| `xmark`  
閉じる  
削除| ![ゴミ箱を表すアイコン。](https://docs-assets.developer.apple.com/published/61f8368d02b05af22d3253a892ced7f3/icons-symbols-meaning-delete%402x.png)| `trash`  
  
### [テキストフォーマット](/jp/design/human-interface-guidelines/icons#Text-formatting)

アクション| アイコン| シンボル名  
---|---|---  
上付き| ![右上隅に数字の1が付いた、大文字のAを表すアイコン。](https://docs-assets.developer.apple.com/published/7e5e3d9b1b0eb6f340f531841d6b27f9/icons-symbols-meaning-superscript%402x.png)| `textformat.superscript`  
下付き| ![右下隅に数字の1が付いた、大文字のAを表すアイコン。](https://docs-assets.developer.apple.com/published/aac330c124cac37a78e02d6049943e53/icons-symbols-meaning-subscript%402x.png)| `textformat.subscript`  
ボールド| ![ボールドで大文字のBを表すアイコン。](https://docs-assets.developer.apple.com/published/c8695e06d6461e79c145e9b6627f70ac/icons-symbols-meaning-bold%402x.png)| `bold`  
イタリック| ![イタリックで大文字のIを表すアイコン。](https://docs-assets.developer.apple.com/published/9f560283ff88d8d1d4b48f278a831b7b/icons-symbols-meaning-italic%402x.png)| `italic`  
アンダーライン| ![アンダーラインが付いた大文字のUを表すアイコン。](https://docs-assets.developer.apple.com/published/3b0d371f10bde381bfa1c9a8999797ec/icons-symbols-meaning-underline%402x.png)| `underline`  
左揃え| ![左端で揃えられた、幅の異なる4本の積み重ねられた水平線を表すアイコン。](https://docs-assets.developer.apple.com/published/68c0ff42aa0ac813b57b663562198e15/icons-symbols-meaning-align-left%402x.png)| `text.alignleft`  
中央揃え| ![中央で揃えられた、幅の異なる4本の積み重ねられた水平線を表すアイコン。](https://docs-assets.developer.apple.com/published/a10b48c850a047efd4a72cc2919c30da/icons-symbols-meaning-align-center%402x.png)| `text.aligncenter`  
両端揃え| ![幅の同じ4本の積み重ねられた水平線を表すアイコン。](https://docs-assets.developer.apple.com/published/d71f35b4f71149b0b908dd1ff8cfe01e/icons-symbols-meaning-align-justified%402x.png)| `text.justify`  
右揃え| ![右端で揃えられた、幅の異なる4本の積み重ねられた水平線を表すアイコン。](https://docs-assets.developer.apple.com/published/8af1da29f8f3173510521492642a82be/icons-symbols-meaning-align-right%402x.png)| `text.alignright`  
  
### [検索](/jp/design/human-interface-guidelines/icons#Search)

アクション| アイコン| シンボル名  
---|---|---  
検索| ![虫眼鏡を表すアイコン。](https://docs-assets.developer.apple.com/published/585f5454757731f942979247bf886ecb/icons-symbols-meaning-search%402x.png)| `magnifyingglass`  
検索| ![書類の上にある虫眼鏡を表すアイコン。](https://docs-assets.developer.apple.com/published/646c6a152822dde685e52a2791ff672f/icons-symbols-meaning-find%402x.png)| `text.page.badge.magnifyingglass`  
検索と置換  
次を検索  
前を検索  
選択部分を検索  
フィルタ| ![上から下へ幅が減少していく3本の積み重ねられた水平線を表すアイコン。](https://docs-assets.developer.apple.com/published/e0924492d663dac952860673a61f4f96/icons-symbols-meaning-filter%402x.png)| `line.3.horizontal.decrease`  
  
### [共有と書き出し](/jp/design/human-interface-guidelines/icons#Sharing-and-exporting)

アクション| アイコン| シンボル名  
---|---|---  
共有| ![正方形の中央から上に向かう矢印を表すアイコン。](https://docs-assets.developer.apple.com/published/b5fa28be3d82955fc380f44783befd32/icons-symbols-meaning-sharing%402x.png)| `square.and.arrow.up`  
書き出す  
プリント| ![プリンタを表すアイコン。](https://docs-assets.developer.apple.com/published/9de4d23e30e6fd8331215dd6dab12878/icons-symbols-meaning-print%402x.png)| `printer`  
  
### [ユーザとアカウント](/jp/design/human-interface-guidelines/icons#Users-and-accounts)

アクション| アイコン| シンボル名  
---|---|---  
アカウント| ![人物の頭と肩を円形の輪郭で抽象的に表現したアイコン。](https://docs-assets.developer.apple.com/published/512c86a1c2c99bc09991c89c1e535441/icons-symbols-meaning-account-user%402x.png)| `person.crop.circle`  
ユーザ  
プロファイル  
  
### [評価](/jp/design/human-interface-guidelines/icons#Ratings)

アクション| アイコン| シンボル名  
---|---|---  
よくないね| ![親指を下に向けたジェスチャの手を表すアイコン。](https://docs-assets.developer.apple.com/published/189b97655ff655985deec03d0466b898/icons-symbols-meaning-dislike%402x.png)| `hand.thumbsdown`  
いいね| ![親指を上に向けたジェスチャの手を表すアイコン。](https://docs-assets.developer.apple.com/published/6f38eef523ffbb4f1d6de22a6a022309/icons-symbols-meaning-like%402x.png)| `hand.thumbsup`  
  
### [レイヤーの順序](/jp/design/human-interface-guidelines/icons#Layer-ordering)

アクション| アイコン| シンボル名  
---|---|---  
最前面へ| ![重なり合った3つの正方形を表すアイコン。一番上の正方形は塗りつぶしスタイル、他の正方形は輪郭で表わされています。](https://docs-assets.developer.apple.com/published/c5da334738c9baf5ddaa0d6ed9de0af6/icons-symbols-meaning-bring-to-front%402x.png)| `square.3.layers.3d.top.filled`  
最背面へ| ![重なり合った3つの正方形を表すアイコン。一番下の正方形は塗りつぶしスタイル、他の正方形は輪郭で表わされています。](https://docs-assets.developer.apple.com/published/1006037b6fa15950ca7ceb933dbb4805/icons-symbols-meaning-send-to-back%402x.png)| `square.3.layers.3d.bottom.filled`  
前面へ| ![重なり合った2つの正方形を表すアイコン。上側の正方形は塗りつぶしスタイル、他方の正方形は輪郭で表わされています。](https://docs-assets.developer.apple.com/published/88b18e0384bca2cd93151169bd507aa3/icons-symbols-meaning-bring-forward%402x.png)| `square.2.layers.3d.top.filled`  
背面へ| ![重なり合った2つの正方形を表すアイコン。下側の正方形は塗りつぶしスタイル、他方の正方形は輪郭で表わされています。](https://docs-assets.developer.apple.com/published/49eb0ed5381249d763d30d4e515bc57b/icons-symbols-meaning-send-backwards%402x.png)| `square.2.layers.3d.bottom.filled`  
  
### [その他](/jp/design/human-interface-guidelines/icons#Other)

アクション| アイコン| シンボル名  
---|---|---  
アラーム| ![目覚まし時計を表すアイコン。](https://docs-assets.developer.apple.com/published/b777cb6bcc99642b037824c78a7efb0e/icons-symbols-meaning-alarm%402x.png)| `alarm`  
アーカイブ| ![ファイルボックスを表すアイコン。](https://docs-assets.developer.apple.com/published/50a3b677d72b3d031ea66d10198bfb59/icons-symbols-meaning-archive%402x.png)| `archivebox`  
カレンダー| ![カレンダーを表すアイコン。](https://docs-assets.developer.apple.com/published/4b14bf07cf562405caebedb2e200e3dc/icons-symbols-meaning-calendar%402x.png)| `calendar`  
  
## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/icons#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOS、watchOSに追加の考慮事項はありません。_

### [macOS](/jp/design/human-interface-guidelines/icons#macOS)

#### [書類アイコン](/jp/design/human-interface-guidelines/icons#Document-icons)

macOSアプリでカスタムの書類のタイプを使用できる場合は、それを表す書類アイコンを作成できます。従来から、書類アイコンは右上隅が折られた紙のような見た目になっています。この固有の見た目により、小さなアイコンであっても、アプリやその他のコンテンツと書類を区別しやすくなります。

対応するファイルタイプに書類アイコンを提供しない場合、macOSはアプリアイコンとファイルの拡張子を組み合わせてアイコンを作成します。例えば「プレビュー」では、システムが生成した書類アイコンを使用してJPGファイルを表しています。

![JPGファイルを表す「プレビュー」の書類アイコンの画像。](https://docs-assets.developer.apple.com/published/bfe462604c63811cb542e7c0fc46185e/doc-icon-generated%402x.png)

アプリでさまざまなファイルタイプを扱う場合は、それを表す一連の書類アイコンを作成する方がよい場合もあります。例えば、Xcodeはカスタムの書類アイコンを使用して、プロジェクト、ARオブジェクト、Swiftコードファイルを区別できるようにしています。

![Xcodeプロジェクトの書類アイコンの画像。](https://docs-assets.developer.apple.com/published/8cd56a7291cd6b41fe391958f704c823/doc-icon-custom-1%402x.png)

![ARオブジェクトの書類アイコンの画像。](https://docs-assets.developer.apple.com/published/a1449177968f693c1bd68c2b146df7c3/doc-icon-custom-2%402x.png)

![Swiftファイルの書類アイコンの画像。](https://docs-assets.developer.apple.com/published/495bd043bf65349ec96f6728941386f8/doc-icon-custom-3%402x.png)

カスタムの書類アイコンを作成するには、背景の塗りつぶし、センター画像、テキストを組み合わせたものを提供します。必要に応じてこれらの要素に対するレイヤーの作成、配置、マスキングが行われた上で、おなじみの角が折られたアイコンの図形が作成されます。

![正方形のキャンバス。ピンク色のグリッド線と、中央を水平方向に伸びるギザギザの白い心電図の線が描かれています。ピンク色のグリッドは、下に向かうほど色が薄くなります。](https://docs-assets.developer.apple.com/published/2aed446834a2dc6e8275b6bd7a797ca9/doc-icon-parts-background-fill%402x.png)背景の塗りつぶし

![塗りつぶされたピンク色のハート。](https://docs-assets.developer.apple.com/published/b59c836903d1b409ab9e21f81762df3e/doc-icon-parts-center-image%402x.png)センター画像

![すべて大文字のHEARTという文字。](https://docs-assets.developer.apple.com/published/56c5adedc0c08a167a4a03e706924ee6/doc-icon-parts-text%402x.png)テキスト

![カスタム書類アイコン。ピンク色のグリッドと白い心電図の線の前面に、ピンク色のハートとHEARTという文字が表示されています。](https://docs-assets.developer.apple.com/published/d5da9148d27f60891780ab1a9546a111/doc-icon-parts%402x.png)macOSでは、提供した要素が組み合わされてカスタムの書類アイコンが生成されます。

[Appleデザインリソース](https://developer.apple.com/design/resources/#macos-apps)では、書類アイコン用のカスタムの背景の塗りつぶしとセンター画像を作成するためのテンプレートが入手できます。このテンプレートを使用する場合は、以下のガイドに従ってください。

**書類のタイプを明確に伝えることができるシンプルな画像をデザインする。** 背景の塗りつぶしやセンター画像を使用するかどうかによらず、シンプルな図形を使用し、カラーの種類を減らすようにします。書類アイコンは16x16 pxまで縮小されて表示される場合があるので、どんなサイズでも認識できるデザインを作成します。

**表現力の高い1つの背景の塗りつぶし画像をデザインすることで、書類のタイプを理解および認識しやすくする。** 例えば、Xcodeとテキストエディットは、どちらも凝った背景画像を使用しており、センター画像は含めていません。

![Xcodeプロジェクトの書類アイコンの画像。](https://docs-assets.developer.apple.com/published/8cd56a7291cd6b41fe391958f704c823/doc-icon-custom-1%402x.png)

![テキストエディットのリッチテキスト書類アイコンの画像。](https://docs-assets.developer.apple.com/published/f32709a5ff5742e79fd03a58ae1dd9c6/doc-icon-fill-only%402x.png)

**小さいバージョンの書類アイコンではシンプルな画像を使用することを検討する。** 大きなバージョンではアイコンの詳細がはっきり見えても、小さいバージョンではぼやけて読みにくくなる場合があります。例えば、中間サイズでカスタムのハートの書類アイコンのグリッド線がよく見えるように、グリッド線を減らし、それに合わせて線を太くします。16x16 pxのサイズでは、完全に線を消してもよいでしょう。

![ハートの書類アイコンを示した画素の荒い画像。グリッド、心電図の線、ハートの図形、HEARTの文字は見えますが、ぼやけています。](https://docs-assets.developer.apple.com/published/1f8bc7946a75363224f373924b557a3a/doc-icon-fewer-details-1%402x.png)32x32 pxのアイコンでは、グリッド線の数が減り、心電図の線が太くなっています。

![ハートの書類アイコンを示した画素の荒い画像。ぼやけたハートの図形と心電図の線だけが表示されています。](https://docs-assets.developer.apple.com/published/e46ac887801d9a16393948c3f2098715/doc-icon-fewer-details-2%402x.png)16x16 px @2xのアイコンでは、心電図の線は残っていますが、グリッド線はありません。

![ハートの書類アイコンを示した画素の荒い画像。ぼやけたハートの図形だけが表示されています。](https://docs-assets.developer.apple.com/published/fd0d2afcd76a9b25c1217ef2ffb1ad0e/doc-icon-fewer-details-3%402x.png)16x16 px @1xのアイコンには、心電図の線とグリッド線はありません。

**背景の塗りつぶしの右上隅に重要なコンテンツを配置しない。** 書類アイコンの形状に収めるため、画像は自動的にマスキングされ、塗りつぶした画像の上隅には折られた白い部分が描画されます。次に示すサイズの背景画像を作成してください。

  * 512x512 px @1x、1024x1024 px @2x

  * 256x256 px @1x、512x512 px @2x

  * 128x128 px @1x、256x256 px @2x

  * 32x32 px @1x、64x64 px @2x

  * 16x16 px @1x、32x32 px @2x

**書類のタイプやアプリとの関連性を伝えることができる身近なアイテムがある場合は、それをセンター画像にすることを検討する。** どんなサイズでもはっきりと認識でき、シンプルで間違われることがない画像をデザインします。センター画像は、書類アイコンのキャンバス全体の半分のサイズです。例えば、32x32 pxの書類アイコンのセンター画像を作成する場合は、16x16 pxの画像キャンバスを使用します。センター画像には、次のサイズを指定できます。

  * 256x256 px @1x、512x512 px @2x

  * 128x128 px @1x、256x256 px @2x

  * 32x32 px @1x、64x64 px @2x

  * 16x16 px @1x、32x32 px @2x

**画像キャンバスの約10%の余白を設け、画像の大半をその内側に収める。** 視覚的な位置合わせのために、画像の一部がこの余白にはみ出しても構いませんが、画像が画像キャンバスの約80%を占めるのが理想的です。例えば、256x256 pxのキャンバスでは、センター画像の大半を205x205 pxの領域に収めます。

![塗りつぶされたピンク色のハートの図形。キャンバスの幅の10%を表す青い余白部分の内側に配置されています。](https://docs-assets.developer.apple.com/published/7cc19b2ae1e99d26ba69e1351683ede1/doc-icon-parts-margins%402x.png)

**書類タイプの理解に役立つ場合は簡単な文字を指定する。** デフォルトで、書類アイコンの下部には書類の拡張子が表示されますが、なじみのない拡張子の場合は説明になる文字を指定することもできます。例えば、SceneKitシーンファイルの書類アイコンでは、ファイルの拡張子である _scn_ ではなく、 _SCENE_ という文字を使用しています。拡張子のテキストは、書類アイコンに収まるように自動的にスケーリングされます。そのため、小さなサイズでも判読できるように、文字は十分短くしてください。デフォルトで、テキストの文字はすべて大文字になります。

![SceneKitシーンの書類アイコンの画像。](https://docs-assets.developer.apple.com/published/3b4bb7de9edb5870d3a162aae8153163/doc-icon-custom-extension%402x.png)

## [リソース](/jp/design/human-interface-guidelines/icons#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/icons#Related)

[アプリアイコン](/jp/design/human-interface-guidelines/app-icons)

[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)

#### [ビデオ](/jp/design/human-interface-guidelines/icons#Videos)

[](https://developer.apple.com/videos/play/wwdc2017/823)

## [変更履歴](/jp/design/human-interface-guidelines/icons#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| 一般的なアクションを表すSF Symbolsの表を追加。  
2023年6月21日| visionOSのガイダンスを追加するために更新。
