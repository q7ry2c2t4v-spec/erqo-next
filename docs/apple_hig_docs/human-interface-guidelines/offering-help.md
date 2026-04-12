# ヘルプの提供

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/offering-help

# ヘルプの提供

親しみやすく直感的に利用できることが理想ではありますが、必要な場合は状況に応じたヘルプを提供できます。

![疑問符のスケッチ。ヘルプが利用可能なことを示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/accec8e899cc002dde40d64d018a3e95/patterns-offering-help-intro%402x.png)

## [ベストプラクティス](/jp/design/human-interface-guidelines/offering-help#Best-practices)

**ユーザに提供するヘルプの種類はアプリのタスクに応じて決める。** 例えば、1つか2つの手順で終わる簡単なタスクであれば、タスクを簡潔に説明したヘルプをインラインで表示するとよいでしょう。逆に、複雑なタスクや複数の手順が必要なタスクがアプリやゲームに用意されている場合は、より大きな目的を達成する方法を説明するチュートリアルを提供することもできます。通常は、ユーザが現在行っているアクションやタスクそのものに直接関係するヘルプを提供します。また、ヘルプは簡単に閉じられるようにし、必要ない場合は表示しないようにしましょう。

**ヘルプで使用する用語や画像には関連性と一貫性を持たせる。** 常に現在の状況に合ったガイドを提供するようにしてください。例えば、tvOS環境でSiri Remoteを使用している場合には、ゲームのコントローラについてのヒントや画像は表示しないようにします。また、プラットフォームに合わせた用語や説明を使用するよう心がけましょう。例えば、iPhoneで「ボタンをクリックする」と表記したり、Macで「メニュー項目をタップする」と表記したりしないようにしてください。

**ヘルプコンテンツではインクルーシブな点に配慮する。** ガイダンスは、[インクルージョン](/jp/design/human-interface-guidelines/inclusion)を参照してください。

**標準のコンポーネントやパターンの仕組みの説明でヘルプコンテンツを肥大化させないようにする。** 代わりに、標準の要素によって実行している、アプリやゲームに固有のアクションやタスクを説明するようにします。独自のコントロール方法を取り入れている場合や、非標準的な方法で入力デバイスを使用する場合は（Siri Remoteを90度回転させた状態で持つなど）、早い段階でユーザに説明するようにします。できれば長い説明ではなく、アニメーションやグラフィックスを使用しましょう。

## [ヒントの作成](/jp/design/human-interface-guidelines/offering-help#Creating-tips)

ヒントは、一時的に表示する小さなビューで、アプリ内の機能の使い方を簡潔に説明するものです。ヒントは、アプリの新機能や目立たない機能について説明する場合や、タスクを早く完了する方法を知らせたい場合に適しています。デベロッパ向けのガイダンスは、[TipKit](https://developer.apple.com/documentation/TipKit)を参照してください。

**アプリのユーザインターフェイスに最も適した種類のヒントを使用する。** コンテンツのフローを維持したいときはポップオーバーヒントを表示し、周囲の情報が確実に表示されるようにしたいときはインラインヒントを表示します。特定のUI要素を指すときは注釈スタイルのインラインヒントを使用でき、UIの特定の部分に関連しないときはヒントスタイルのヒントを使用できます。

![iPhoneのポップオーバースタイルのヒントの図。ヒントは近くにあるコンテンツの上に表示され、青い星のアイコンで表現された機能を指しています。ヒントの下のコンテンツは隠れています。](https://docs-assets.developer.apple.com/published/7ee5bc8e67df2cdaa103e7728effa644/offering-help-tip-popover%402x.png)

ポップオーバー

![iPhoneの注釈スタイルのヒントの図。ヒントは周囲のコンテンツの中に埋め込まれ、青い星のアイコンで表現された機能を指しています。動かされたテキストはヒントの上と下に表示されます。](https://docs-assets.developer.apple.com/published/611889edf02e0809a58a17df09e1b4c7/offering-help-tip-annotation%402x.png)

注釈

![iPhoneのヒントスタイルのヒントの図。ヒントは周囲のコンテンツの中に埋め込まれています。動かされたテキストはヒントの上と下に表示されます。](https://docs-assets.developer.apple.com/published/674068d7dd7d1cffaef6bc644994edf8/offering-help-tip-hint%402x.png)

ヒント

**ヒントは簡単な機能に使用する。** ヒントが一番向いているのは、説明しやすく、いくつかの簡単な手順で完了できる機能です。3つを上回る数のアクションが必要な機能は、ヒントには複雑すぎる可能性があります。

**短くて、操作したくなるような、惹きつけられるヒントにする。** ヒントの目的は、ユーザに新機能を試してもらうことです。直接的で操作中心の言葉を使用して、機能の内容とその使い方を説明します。ヒントは1文か2文にとどめ、宣伝的なコンテンツや別の機能またはユーザフローに関係するコンテンツは含めないようにします。宣伝的なコンテンツとは、広告や販売に関連するものや、現在ユーザが行っている作業と合致しないものを指します。

**ヒントが意図したユーザに届くようにルールを定める。** すべてのヒントがすべてのユーザに役立つわけではありません。例えば、すでに対象の機能を使っているユーザは、それを説明するヒントを見たいとは思わないでしょう。パラメータやイベントに基づいてヒントの適格性を決めるルールを設け、ヒントを表示するタイミングを調整したり、ヒントが役立つと思われるユーザだけに表示したりします。アプリに複数のヒントがある場合は、表示頻度を設定し、例えば24時間ごとなど、妥当な周期でヒントが表示されるようにします。

**機能に関連する画像やシンボルがある場合は、ヒントに含めることを検討し、できる限り塗りつぶされたバリアントを使用する。** 例えば、星が付いたヒントなら、ヒントがお気に入りに関連するものだと理解しやすくなります。

![ヒントスタイルのヒントの図。先頭側に塗りつぶされていない青い星のシンボルがあります。](https://docs-assets.developer.apple.com/published/d0e2e17156edee5cd85db2207777bd42/offering-help-tip-symbol-usage-unfilled-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![ヒントスタイルのヒントの図。先頭側に塗りつぶされた青い星のシンボルがあります。](https://docs-assets.developer.apple.com/published/1974ce07389b1a56f9ddbb4c5477c75d/offering-help-tip-symbol-usage-filled-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

ヒントが直接つながっていない画像で機能が表現されている場合は、ヒントとUIの両方で同じ画像を繰り返し使用しないようにしてください。

![注釈スタイルのヒントの図。青い星のアイコンで表現された機能を指しています。ヒントの先頭側には同じような青い星のシンボルがあります。](https://docs-assets.developer.apple.com/published/38e8501ef2322fd210faef280d2b9524/offering-help-tip-symbol-usage-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![注釈スタイルのヒントの図。青い星のアイコンで表現された機能を指しています。ヒントはテキストのみで、添えられるシンボルは省かれています。](https://docs-assets.developer.apple.com/published/bf9749275bf01ee8435f5d7ffca96824/offering-help-tip-symbol-usage-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**ボタンを使用して情報やオプションに誘導する。** 機能にカスタマイズできる設定がある場合や、機能についてさらに詳しく知ることができる領域に誘導したい場合は、ボタンを追加することを検討します。ボタンを使用すると、ユーザを直接設定に誘導し、調整を行ってもらえます。または、ほかに役立つ情報がある場合は、ボタンを追加して、設定フローなどの追加リソースに誘導します。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/offering-help#Platform-considerations)

 _iOS、iPadOS、tvOS、watchOSに追加の考慮事項はありません。_

### [macOS、visionOS](/jp/design/human-interface-guidelines/offering-help#macOS-visionOS)

 _ツールチップ_ （ユーザ向けドキュメントでは _ヘルプタグ_ とも呼ばれます）は、一時的に表示される小さなビューで、インターフェイス内のコンポーネントの使い方を簡潔に説明するものです。iPhoneやiPadのアプリも含め、Macで動作するアプリでは、ユーザが要素にポインタを合わせるとツールチップが表示されます。visionOSアプリでは、ユーザが要素を見つめるか、要素にポインタを合わせるとツールチップが表示されます。デベロッパ向けのガイダンスは、[`help(_:)`](/documentation/SwiftUI/View/help\(_:\)-6oiyb)を参照してください。

![macOSのFinderのツールバーの図。「戻る」ボタンの上にポインタがあります。ポインタの下に、以前に表示したフォルダを表示するというタイトルのヒントが表示されています。](https://docs-assets.developer.apple.com/published/67521952664413054d6e4fd102a3279a/offering-help-macos-tooltip-help-tag%402x.png)

**ユーザが注目しているコントロールについてのみ説明する。** 特定のコントロールの使い方を知りたいユーザは、近辺のコントロールの使い方や大きなタスクの実行方法を知りたいわけではありません。

**そのコントロールによって開始されるアクションやタスクを説明する。** 多くの場合、説明に動詞を含めるとよいでしょう。例えば、「デフォルト設定に復元」や「リストの言語を追加/削除」のようにします。

**ツールチップでは、基本的にコントロールの名前を繰り返さない。** 名前を繰り返してもツールチップの場所を取るだけで、説明が改善されることはまずありません。

**簡潔にする。** できる限り、ツールチップのコンテンツは最大でも60字から75字に収めるようにします（ローカリゼーションによってテキストの長さが変わることが多い点に注意してください）。説明が簡潔かつ直接的になるように、体言止めのような簡潔な表現を使用することを検討してください。長いテキストでないとコントロールを説明できない場合は、インターフェイスのデザインをシンプルにすることを検討してください。

**センテンススタイルを使う。** 普通は、センテンススタイルの方が気軽に利用しやすい印象を与えます。完全な文で書く場合は、アプリのスタイルとの一貫性を保つ上で必要でない限り、文末の句読点は省きます。

**状況に応じたツールチップにすることを心掛ける。** 例えば、コントロールの状態に応じて表示するテキストを変えることができます。

## [リソース](/jp/design/human-interface-guidelines/offering-help#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/offering-help#Related)

[オンボーディング](/jp/design/human-interface-guidelines/onboarding)

[フィードバック](/jp/design/human-interface-guidelines/feedback)

[表現](/jp/design/human-interface-guidelines/writing)

[「ヘルプ」メニュー](/jp/design/human-interface-guidelines/the-menu-bar#Help-menu)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/offering-help#Developer-documentation)

[TipKit](/documentation/TipKit)

[`NSHelpManager`](/documentation/AppKit/NSHelpManager) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/offering-help#Videos)

[](https://developer.apple.com/videos/play/wwdc2023/10229)

## [変更履歴](/jp/design/human-interface-guidelines/offering-help#Change-log)

日付| 変更内容  
---|---  
2023年12月05日| ツールチップを作成するためのガイダンスにvisionOSを追加。  
2023年9月12日| ヒント作成のガイダンスを追加。
