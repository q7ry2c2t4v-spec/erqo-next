# 右から左

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/right-to-left

# 右から左

アラビア語やヘブライ語などの右から左に記述される言語に対応するには、関連するスクリプトを読む方向に合わせるために、必要に応じてインターフェイスの左右の配置/揃えを逆にします。

![ウインドウの中で右揃えの箇条書きリストのスケッチ。右から左に記述する言語でのインターフェイスの提案を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる黄色になっています](https://docs-assets.developer.apple.com/published/cee2b03a2a46879f5fd310c9a7027449/foundations-rtl-intro%402x.png)

ユーザはデバイス（あるいはアプリまたはゲームのみ）の言語を選択したとき、インターフェイスがさまざまな方法でそれに適応することを期待します（詳しくは、[ローカリゼーション](https://developer.apple.com/localization/)を参照してください）。

システムで提供されるUIフレームワークはデフォルトで右から左（RTL）に対応しているため、システムで提供されるUIコンポーネントはRTLコンテキストで自動的に左右の配置/揃えを逆にできます。システムで提供される要素と標準レイアウトを使用すれば、自動的に左右の配置/揃えを逆にするアプリのインターフェイスに変更を加える必要がない場合があります。

RTLの言語が使用される国のさまざまなロケールで出現する可能性がある異なる通貨、数字、数学記号に適応するために、レイアウトを微調整したり、特定のローカリゼーションを強化したりしたい場合は、以下のガイドラインに従ってください。

## [テキストの配置](/jp/design/human-interface-guidelines/right-to-left#Text-alignment)

**インターフェイスの方向に合わせてテキストの配置を調整する（システムで自動的に行われない場合）。** 例えば、左から右（LTR）のコンテキストのコンテンツでテキストを左揃えにする場合、RTLコンテキストでは左右の配置/揃えを逆にしたコンテンツの位置に合わせてテキストを右揃えにします。

![インターフェイスに表示されているテキストと画像のレイアウトを示す図。角丸四角形の領域の上で、テキストを表す3本のバーが左揃えになっています。その領域の中心にプレースホルダ画像、その下に別のバーがあります。領域内のバーは左揃えです。](https://docs-assets.developer.apple.com/published/74011ec08edc18372f19903b92b55dba/text-alignment-ltr-screen%402x.png)LTRコンテキストでの左揃えのテキスト

![インターフェイスに表示されているテキストと画像のレイアウトを示す図。角丸四角形の領域の上で、テキストを表す3本のバーが右揃えになっています。その領域の中心にプレースホルダ画像、その下に別のバーがあります。領域内のバーは右揃えです。プレースホルダ画像は反転されません。](https://docs-assets.developer.apple.com/published/0417badeb6913b72ea90102937072fd1/text-alignment-rtl-screen%402x.png)RTLコンテキストでの右揃えのテキスト

**現在のコンテキストではなく、段落の言語に合わせて段落を配置する。** 段落（3行以上のテキストで定義される）の配置が段落の言語に一致していないと、読みにくい場合があります。例えば、LTRのテキストで構成される段落を右揃えすると、各行の先頭が見づらくなります。読みやすくするため、1行または2行のテキストブロックは引き続き現在のコンテキストでの読む方向に合わせて配置しますが、段落の場合はその言語に合わせて配置します。

![プレースホルダコピーの2つの段落を表示している画像。最初の段落はアラビア語で、右揃えになっています。2番目の段落は英語で、左揃えになっています。](https://docs-assets.developer.apple.com/published/2ed90e1ec349fa6da401eee0b2fcb74f/paragraph-alignment-correct%402x.png)RTLコンテキストでの左揃えの段落

![丸に囲まれたチェックマークが適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![プレースホルダコピーの2つの段落を表示している画像。最初の段落はアラビア語で、2番目の段落は英語です。両方の段落が右揃えになっています。](https://docs-assets.developer.apple.com/published/c6fe428387278d43f240b4b58ff7295d/paragraph-alignment-wrong%402x.png)RTLコンテキストでの右揃えの段落

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**リスト内のすべてのテキスト項目に一貫した配置を使用する。** 読んだりスキャンしたりする体験を快適にするには、別のスクリプトで表示される項目も含め、リスト内の全項目の左右の配置を揃えます。

![右から左に記述されるテキストを表すグレイのバーの右揃えのリストの図。](https://docs-assets.developer.apple.com/published/8e497bdc80a98b7896b492d2e5bfb57b/mixed-script-list-alignment-correct%402x.png)RTLコンテキストでの右揃えのテキスト

![丸に囲まれたチェックマークが適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![グレイのバーのリストの図。1番目、3番目、4番目、5番目のバーは、右から左に記述されるテキストを表します。2番目のバーが誤って左揃えになっています。](https://docs-assets.developer.apple.com/published/8764f467c4870522419bb26fa5894c09/mixed-script-list-alignment-wrong%402x.png)RTLコンテキストで混在する配置

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

## [数字と文字](/jp/design/human-interface-guidelines/right-to-left#Numbers-and-characters)

さまざまなRTL言語で異なる記数法が使用される場合があります。例えば、ヘブライ語のテキストでは西アラビア数字が使用され、アラビア語のテキストでは西アラビア数字が使用される場合とインド数字が使用される場合があります。西アラビア数字とインド数字のどちらが使用されるかは、国や地域によって、さらには同じ国や地域内の場所によって異なります。

アプリで数学的な概念や、数字が鍵になるその他のトピックを扱う場合は、対応するロケールごとにそのような情報を適切に表示する方法を明らかにすることをおすすめします。これに対し、数字関連のトピックを扱わないアプリでは通常、システムで提供される数の表記に依存できます。

![左から、数字の1、2、そして西アラビア数字の3。](https://docs-assets.developer.apple.com/published/c40d3d208a9aee56d680d6915fb44fff/textformat-123-ltr%402x.png)西アラビア数字

![右から、数字の1、2、そしてインド数字の3。](https://docs-assets.developer.apple.com/published/8a9f9c2f6fb291304a5d93e27be0bead/textformat-123-ar%402x.png)インド数字

**特定の番号では数字を逆順にしない。** 電話番号の「541」やクレジットカード番号などの特定の番号の数字は、現在の言語や周囲のコンテンツにかかわらず、常に同じ順序で表示されます。

![左から、ラテン文字スクリプトでの「order」（注文）と「number」（番号）の2単語、その後ろに数字の123456。](https://docs-assets.developer.apple.com/published/e6ae8d9dab2a6da825829cf88bfb6adb/latin-numerals%402x.png)ラテン文字

![右から、ヘブライ文字スクリプトでの「order」と「number」の2単語、その後ろに数字の12345。](https://docs-assets.developer.apple.com/published/8b4b0b82384424720d861865ac61ad37/hebrew-numerals%402x.png)ヘブライ文字

![右から、アラビア文字スクリプトでの「order」と「number」の2単語、その後ろに西アラビア数字の12345。](https://docs-assets.developer.apple.com/published/4ce7e1cd6311618855836a92f106537a/western-arabic-numerals%402x.png)アラビア文字（西アラビア数字）

![右から、アラビア文字スクリプトでの「order」と「number」の2単語、その後ろにインド数字の12345。](https://docs-assets.developer.apple.com/published/71bff39a696a02a3fc6c39defb442384/eastern-arabic-numerals%402x.png)アラビア文字（インド数字）

**進行状況またはカウントの方向を示す数字は逆順にし、数字自体は反転させない。** 進行状況バー、スライダ、評価コントロールなどのコントロールには、意味を明瞭にするために数字が含まれることがよくあります。数字をこのように使用する場合は、反転したコントロールの向きに合わせて必ず数字を逆順にしてください。また、数字のシーケンスを使って特定の順序を伝える場合は、シーケンスを逆順にします。

![横1列に並んだ5つの星。左から、最初の3つ半の星が塗りつぶされています。星の下にはローマ数字が縦に並んでいて、それぞれの位置が上の星に揃えられています。数字は左から順に1、2、3、4、5です。](https://docs-assets.developer.apple.com/published/d249f8e9df8a8dfcf1526dc3f5c4dd5b/match-numeral-order-to-directional-controls-latin%402x.png)ラテン文字

![横1列に並んだ5つの星。右から、最初の3つ半の星が塗りつぶされています。星の下にはインド数字が縦に並んでいて、それぞれの位置が上の星に揃えられています。数字は右から順に1、2、3、4、5です。](https://docs-assets.developer.apple.com/published/77bb1e2c8c704fa2235bd7cc8d7acf31/match-numeral-order-to-directional-controls-eastern-arabic%402x.png)アラビア文字（インド数字）

![横1列に並んだ5つの星。右から、最初の3つ半の星が塗りつぶされています。星の下には西アラビア数字が縦に並んでいて、それぞれの位置が上の星に揃えられています。数字は右から順に1、2、3、4、5です。](https://docs-assets.developer.apple.com/published/164c27556e186de5aa0c0312639f1c8f/match-numeral-order-to-directional-controls-western-arabic-hebrew%402x.png)ヘブライ文字

![横1列に並んだ5つの星。右から、最初の3つ半の星が塗りつぶされています。星の下には西アラビア数字が縦に並んでいて、それぞれの位置が上の星に揃えられています。数字は右から順に1、2、3、4、5です。](https://docs-assets.developer.apple.com/published/164c27556e186de5aa0c0312639f1c8f/match-numeral-order-to-directional-controls-western-arabic-hebrew%402x.png)アラビア文字（西アラビア数字）

## [コントロール](/jp/design/human-interface-guidelines/right-to-left#Controls)

**1つの値から別の値への進行を示すコントロールは反転させる。** ユーザは前方への進行を自分が読む言語と同じ方向の動きと見なす傾向があるため、RTLコンテキストではスライダやプログレスインジケータなどのコントロールを反転させた方がよいでしょう。反転させる場合は、コントロールに付随して最初と最後の値を表すグリフや画像の位置も必ず逆にしてください。

![音量コントロールのスライダの図。左側には音が出ていない右向きのスピーカーのグリフ、右側には右向きのスピーカーのグリフとそこから発している音波があり、つまみを左から右に動かして音量を大きくしています。](https://docs-assets.developer.apple.com/published/7ef757b48788617e37c2a275b6b47f6d/flipped-directional-control-ltr%402x.png)LTRコンテキストでの方向のあるコントロール

![音量コントロールのスライダの図。右側には音が出ていない左向きのスピーカーのグリフ、左側には左向きのスピーカーのグリフとそこから発している音波があり、つまみを右から左に動かして音量を大きくしています。](https://docs-assets.developer.apple.com/published/b5619e5a9fb04db70e26dac8c20313b2/flipped-directional-control-rtl%402x.png)RTLコンテキストでの方向のあるコントロール

**ユーザが移動したり決まった順序で項目にアクセスしたりできるようにするコントロールは反転させる。** 例えば、RTLコンテキストでは戻るボタンを右向きにして、RTLの言語を読む方向と画面の流れを一致させる必要があります。同様に、順序付けされたリストの項目にユーザがアクセスできるようにする「次へ」ボタンや「戻る」ボタンも、RTLコンテキストでは読む方向に合わせて反転させる必要があります。

**実際の方向または画面上の特定の領域を指すコントロールの向きは維持する。** 例えば「右へ」という意味のコントロールを表示する場合、そのコントロールは現在のコンテキストにかかわらず常に右を指す必要があります。

**必要に応じて、隣り合うラテン文字スクリプトとRTLスクリプトの視覚的なバランスを取る。** ボタン、ラベル、タイトルでは、アラビア文字またはヘブライ文字のテキストを大文字ラテン文字の横に配置すると、小さすぎるように見えることがあります。アラビア文字とヘブライ文字には大文字が含まれないからです。アラビア文字またはヘブライ文字のテキストとすべて大文字のラテン文字のテキストとの視覚的なバランスを取るには、多くの場合RTLのフォントサイズを2ポイントほど大きくするとうまくいきます。

![横1列に並んだ3つの青い長円形のボタン。各ボタンにダウンロードという単語のラベルが付いています。ラベルは左から順にラテン文字、アラビア文字、ヘブライ文字のスクリプトで、英語のラベルではすべて大文字が使用されています。2本の赤い横線が3つのボタンすべてを横切っていて、上の線はアセンダライン、下の線はベースラインです。英語のラベルでは、すべての文字が両方の線に接しています。アラビア文字のラベルでは、最後の2文字のみがベースラインに接しているか下に突き抜けていますが、アセンダラインに接しているのは最後の文字だけです。ヘブライ文字のラベルでは、すべての文字がどちらの線にも接していません。ラテン文字のラベルと比べると、アラビア文字とヘブライ文字のラベルは小さく見えます。](https://docs-assets.developer.apple.com/published/190b48a71d8d934047905be986732fb4/download-uneven-vertical-height%402x.png)アラビア文字とヘブライ文字のテキストは、同じフォントサイズの大文字ラテン文字のテキストの横では小さすぎるように見える場合があります。

![横1列に並んだ3つの青い長円形のボタン。各ボタンにダウンロードという単語のラベルが付いています。ラベルは左から順にラテン文字、アラビア文字、ヘブライ文字のスクリプトで、英語のラベルではすべて大文字が使用されています。2本の赤い横線が3つのボタンすべてを横切っていて、上の線はアセンダライン、下の線はベースラインです。英語のラベルでは、すべての文字が両方の線に接しています。アラビア文字のラベルでは、最後の2文字のみがベースラインに接しているか下に突き抜けていて、最後の文字はアセンダラインの上に突き抜けています。ヘブライ文字のラベルでは、すべての文字がベースラインに接していて、アセンダラインにも接しています。アラビア文字とヘブライ文字のラベルのサイズを大きくすると、ラテン文字のラベルと同じようなサイズに見えます。](https://docs-assets.developer.apple.com/published/19099f313875cd49849a1ca28f1dfca4/download-even-vertical-height%402x.png)アラビア文字とヘブライ文字のテキストのフォントサイズをわずかに大きくすることで、大文字ラテン文字のテキストと視覚的にバランスが取れます。

## [画像](/jp/design/human-interface-guidelines/right-to-left#Images)

**写真、イラスト、一般的なアートワークなどの画像は反転させない。** 画像を反転させると、多くの場合画像の意味が変わってしまいます。著作権のある画像を反転させると、著作権を侵害するおそれがあります。画像の内容が読む方向と強く結び付いている場合は、オリジナルを反転させるのではなく、新しいバージョンの画像を作成することを検討してください。

![単純化された地球の図。アフリカ、ヨーロッパ、アジア、オーストラリア、南極大陸のほとんどが黒い無地の図形で示されています。](https://docs-assets.developer.apple.com/published/ca80fd6003c4ebff97714123a33c974e/image-displayed-right%402x.png)

![丸に囲まれたチェックマークが適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![単純化された地球の図。東半球が横方向に反転していて、アフリカが右端、オーストラリアが左端に表示されています。](https://docs-assets.developer.apple.com/published/0310648a2b1ff40a796e5544d057d30b/image-displayed-wrong%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**画像の順序に意味がある場合は画像の位置を逆にする。** 例えば、複数の画像を時系列順、アルファベット順、お気に入り順などの特定の順序で表示する場合、RTLコンテキストでは画像の位置を逆にして順序の意味を保持します。

![角丸四角形の中のテキストと画像のレイアウトを示す図。テキストを表す短いバーが左上隅で左揃えになっています。バーの下には、プレースホルダ画像が入った左側の青い正方形など、4つの正方形を含む領域があります。四角形の一番下には5つの正方形が並んでいて、左から順にハート、円、星、正方形、三角形の図形が入っています。](https://docs-assets.developer.apple.com/published/49dc1b87f367d75c21592b4016239b6b/image-positions-ltr%402x.png)LTRコンテキストでの位置に意味がある項目

![角丸四角形の中のテキストと画像のレイアウトを示す図。テキストを表す短いバーが右上隅で右揃えになっています。バーの下には、プレースホルダ画像が入った右側の青い正方形など、4つの正方形を含む領域があります。四角形の一番下には5つの正方形が並んでいて、右から順にハート、円、星、正方形、三角形の図形が入っています。](https://docs-assets.developer.apple.com/published/6d82352b45486ccd4d9a28a74077e996/image-positions-rtl%402x.png)RTLコンテキストでの位置に意味がある項目

## [インターフェイスアイコン](/jp/design/human-interface-guidelines/right-to-left#Interface-icons)

[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)を使ってアプリのインターフェイスアイコンを利用する場合は、RTLコンテキスト用のバリエーションとアラビア語やヘブライ語などの言語用にローカライズされたシンボルを利用できます。カスタムシンボルを作成する場合は、その方向性を指定できます。デベロッパ向けのガイダンスは、[アプリのカスタムシンボル画像の作成](/documentation/UIKit/creating-custom-symbol-images-for-your-app)を参照してください。

![等間隔で積み重なった3本の横線。それぞれの線の行頭記号が左側にあります。背表紙が左側にある閉じた本の図形。左揃えの3つの点を含む角丸四角形。鉛筆が約45度傾いていて、先端が右端の点の右にあり、消しゴムが四角形の右上隅から突き出ています。上部に黒いバーがある角丸四角形。バーは四角形の高さの約4分の1を占めています。バーの中の左側には白い点が左揃えで並んでいます。左端付近に小さな黒い無地の四角形が入っている角丸四角形。角丸四角形の外の右側に黒い無地の半円があり、その縦の直線が四角形の右端の縦線に近接しています。](https://docs-assets.developer.apple.com/published/572736b0904fcdb886b054c7ad3fb3f1/directional-symbols-ltr%402x.png)方向のあるシンボルのLTRバリエーション

![等間隔で積み重なった3本の横線。それぞれの線の行頭記号が右側にあります。背表紙が右側にある閉じた本の図形。右揃えの3つの点を含む角丸四角形。鉛筆が約45度傾いていて、先端が左端の点の左にあり、消しゴムが四角形の上辺の中央から突き出ています。上部に黒いバーがある角丸四角形。バーは四角形の高さの約4分の1を占めています。バーの中の右側には白い点が右揃えで並んでいます。右端付近に小さな黒い無地の四角形が入っている角丸四角形。角丸四角形の外の左側に黒い無地の半円があり、その縦の直線が四角形の左端の縦線に近接しています。](https://docs-assets.developer.apple.com/published/03ccea2e8bce53ed3ebf66f79477568b/directional-symbols-rtl%402x.png)方向のあるシンボルのRTLバリエーション

**テキストまたは読む方向を表すインターフェイスアイコンは反転させる。** 例えば、LTRコンテキストでテキストを表す左揃えのバーをインターフェイスアイコンで使用する場合、RTLコンテキストではバーを右揃えにします。

![左揃えの3本の横線を含む角丸四角形。](https://docs-assets.developer.apple.com/published/298befd594e841846cd466f60d2bea6a/doc-plaintext-ltr%402x.png)テキストを表すシンボルのLTRバリエーション

![右揃えの3本の横線を含む角丸四角形。](https://docs-assets.developer.apple.com/published/bfae7054f6aec52f1a63e31b6c0db79d/doc-plaintext-rtl%402x.png)テキストを表すシンボルのRTLバリエーション

**テキストを含むインターフェイスアイコンのローカライズバージョンの作成を検討する。** 一部のインターフェイスアイコンには、フォントサイズの選択や署名など、文字やテキストに関わる概念を伝えるための文字や単語が含まれます。カスタムインターフェイスアイコンで文字を含める必要がある場合は、ローカライズバージョンを作成することを検討してください。例えばSF Symbolsには、ラテン文字、ヘブライ文字、アラビア文字などに使用できるさまざまなバージョンの署名、リッチテキスト、Iビームポインタが用意されています。

![横線の上で左揃えになっている小さなX。図案化された署名がそのXから始まり、線の右端で終わっています。左上隅に大文字のA、右上隅に積み重なった2本の横線がある角丸四角形。四角形の下半分にはプレースホルダ画像が表示されています。背の高いIビームカーソルの左にある大きな大文字のA。](https://docs-assets.developer.apple.com/published/431f27ff945804173931cfd38f595b2c/text-icon-localized-latin%402x.png)ラテン文字

![横線の上で右揃えになっている小さなX。図案化された署名がそのXから始まり、線の左端で終わっています。右上隅にアレフという文字、左上隅に積み重なった2本の横線がある角丸四角形。四角形の下半分にはプレースホルダ画像が表示されています。背の高いIビームカーソルの左にある大きなアレフという文字。](https://docs-assets.developer.apple.com/published/b457fc7b677ccbf085cd1ea1d8bc5601/text-icon-localized-hebrew%402x.png)ヘブライ文字

![横線の上で右揃えになっている小さなX。図案化された署名がそのXから始まり、線の左端で終わっています。右上隅にアインという文字、左上隅に積み重なった2本の横線がある角丸四角形。四角形の下半分にはプレースホルダ画像が表示されています。背の高いIビームカーソルの左にある大きなダードという文字。](https://docs-assets.developer.apple.com/published/6c81b23024e731b6e79f592b49e9c4d3/text-icon-localized-arabic%402x.png)アラビア文字

読み書きとは関係のない概念を伝えるために文字や単語を使用するカスタムインターフェイスアイコンがある場合は、テキストを使用しない代替画像をデザインすることを検討してください。

**前方または後方への動きを示すインターフェイスアイコンは反転させる。** ユーザが文字を読むのと同じ方向に何かが動くとき、ユーザは通常その方向を前方と解釈します。何かがその反対の方向に動く場合は、その方向を後方と解釈する傾向があります。前方または後方に移動するオブジェクトを表すインターフェイスアイコンは、RTLコンテキストでは動きの意味を保持するために反転させる必要があります。例えば、スピーカーを表すアイコンには、一般にスピーカーから前方に発する音波が表示されます。LTRコンテキストでは音波が左から出ているため、RTLコンテキストではアイコンを反転させて音波が右から出るように表示する必要があります。

![スピーカーの輪郭。3本の同心円状の曲線が右方向に発しています。](https://docs-assets.developer.apple.com/published/d43d629eea61239a9268d6616551b48c/speaker-wave-3-ltr%402x.png)前方への動きを表すシンボルのLTRバリエーション

![スピーカーの輪郭。3本の同心円状の曲線が左方向に発しています。](https://docs-assets.developer.apple.com/published/d10bb4c00b214c16a802183377134b59/speaker-wave-3-rtl%402x.png)前方への動きを表すシンボルのRTLバリエーション

**ロゴまたはユニバーサルなサインやマークは反転させない。** 反転させたロゴを表示するとユーザの混乱を招き、法的な影響が生じる可能性もあります。ロゴは、テキストが入っている場合も含め常にオリジナルの形状で表示します。ユーザはチェックマークなどのユニバーサルな記号やマークの表示に一貫性を期待しているため、反転させないでください。

![黒いApple TVロゴを含む角丸四角形。ロゴでは小文字のTとVの左に黒い無地のリンゴが描かれています。](https://docs-assets.developer.apple.com/published/7c7eb6d19b63d77412c7754893c0f65c/appletv-ltr%402x.png)ロゴ

![チェックマーク。](https://docs-assets.developer.apple.com/published/31cfb3b8b93a1747eddac562a979a9cb/checkmark-ltr%402x.png)ユニバーサルな記号またはマーク

**一般に、現実世界のオブジェクトを表すインターフェイスアイコンは反転させない。** 方向性を示すオブジェクトを使用する場合を除き、なじみのあるアイテムを表すアイコンは反転を避けるのが最善です。例えば、時計の仕組みはどこでも同じなので、伝統的な時計のインターフェイスアイコンは言語の方向にかかわらず同じにする必要があります。一部のインターフェイスアイコンは、右利き用に傾倒したアイテムであり、それが言語または読む方向が基準にされている印象を与えることがあります。ただし、ほとんどの人は右利きであるため、右利き用のツールを示すアイコンを反転させる必要はなく、反転させると混乱を招くおそれがあります。

![2本の白線が9時の位置にある黒いディスク。](https://docs-assets.developer.apple.com/published/2d167db99027c9f44270a86a273f225f/clock-fill-ltr%402x.png)

![消しゴム付きの鉛筆。先端を下にして約45度右下に傾いています。](https://docs-assets.developer.apple.com/published/6597719e77e19638bb265cd6c58f9a8a/pencil-ltr%402x.png)

![ゲームコントローラのシルエット。左側に白いプラス記号、右側に2つの白いボタンがあります。](https://docs-assets.developer.apple.com/published/c3f51c228de248bf096aae7164836eab/gamecontroller-fill-ltr%402x.png)

**カスタムインターフェイスアイコンを単に反転させる前に、個別のコンポーネント間と全体の視覚的バランスを考慮に入れる。** 場合によっては、バッジ、スラッシュ、虫眼鏡などのコンポーネントを、ローカリゼーションにかかわらずビジュアルデザイン言語に準拠させる必要があります。例えばSF Symbolsでは、シンボルの意味の禁止または否定を表すためにLTRバージョンでもRTLバージョンでも同じバックスラッシュを使用して、視覚的な一貫性を保っています。

![右向きのスピーカーのシルエット。その上にバックスラッシュが重なっています。](https://docs-assets.developer.apple.com/published/0557fd6fd8fc1b2c347cd869baa6ae0e/speaker-slash-fill-ltr%402x.png)バックスラッシュを含むシンボルのLTRバリエーション

![左向きのスピーカーのシルエット。その上にバックスラッシュが重なっています。](https://docs-assets.developer.apple.com/published/42dc822fc59ebc4c8d02d6e6c7fa0959/speaker-slash-fill-rtl%402x.png)バックスラッシュを含むシンボルのRTLバリエーション

また、ローカライズしたバージョンのアイコンでも意味をなすように、コンポーネント（またはその位置）を反転させる必要が生じる場合もあります。例えば、実際にユーザに表示されるUIを表すバッジの場合、UIが反転していればバッジも反転させる必要があります。また、バッジによってインターフェイスアイコンの意味が変わる場合は、バッジを反転させても変更後の意味とアイコン全体の視覚的バランスの両方を保持できるかどうかを検討してください。下に表示されている画像ではバッジにUIのオブジェクトが描かれませんが、プラス記号を右上隅のままにするとカートの視覚的なバランスが損なわれます。

![右向きの車輪付きショッピングカートのシルエット。右上隅には黒いディスクに入った白いプラス記号があります。](https://docs-assets.developer.apple.com/published/faa9849953c7b1b1470db91ed25125d0/cart-fill-badge-plus-ltr%402x.png)

![丸に囲まれたチェックマークが適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![左向きの車輪付きショッピングカートのシルエット。右上隅には黒いディスクに入った白いプラス記号があります。](https://docs-assets.developer.apple.com/published/c065f8369e681461bc34ea590b80994b/cart-fill-badge-rtl-unbalanced%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![左向きの車輪付きショッピングカートのシルエット。左上隅には黒いディスクに入った白いプラス記号があります。](https://docs-assets.developer.apple.com/published/97251e1850265c3b1d654d1e4631ca74/cart-fill-badge-plus-rtl%402x.png)

![丸に囲まれたチェックマークが適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

右利きの利用を暗示するツールなどのコンポーネントがカスタムインターフェイスに含まれる場合は、必要に応じてベース画像を反転させても、ツール自体の向きを保持することを検討してください。

![右上隅に黒い点がある角丸四角形。点の左側では、積み重なった2本の左揃えの線を含む虫眼鏡が四角形に重なっていて、約135度傾いています。](https://docs-assets.developer.apple.com/published/0c8dd8148be262162bb75a017e2ae197/mail-and-text-magnifyingglass-ltr%402x.png)道具を表すシンボルのLTRバリエーション

![左上隅に黒い点がある角丸四角形。点の右側では、積み重なった2本の右揃えの線を含む虫眼鏡が四角形に重なっていて、約135度傾いています。](https://docs-assets.developer.apple.com/published/f3ca739120456691b67e55d150596716/mail-and-text-magnifyingglass-rtl%402x.png)道具を表すシンボルのRTLバリエーション

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/right-to-left#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOS、watchOSに追加の考慮事項はありません。_

## [リソース](/jp/design/human-interface-guidelines/right-to-left#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/right-to-left#Related)

[レイアウト](/jp/design/human-interface-guidelines/layout)

[インクルージョン](/jp/design/human-interface-guidelines/inclusion)

[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/right-to-left#Developer-documentation)

[ローカリゼーション](https://developer.apple.com/localization/)

[ビューのローカリゼーションへの対応](/documentation/SwiftUI/Preparing-views-for-localization) — SwiftUI

#### [ビデオ](/jp/design/human-interface-guidelines/right-to-left#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/222)

[](https://developer.apple.com/videos/play/wwdc2022/10034)
