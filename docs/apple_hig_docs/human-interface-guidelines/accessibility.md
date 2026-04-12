# アクセシビリティ

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/accessibility

# アクセシビリティ

アクセシブルなユーザインターフェイスでは、あらゆる人がアプリやゲームを楽しめます。

![「アクセシビリティ」アイコンのスケッチ。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる黄色になっています](https://docs-assets.developer.apple.com/published/766247a328e34933bd6368d48970c8b8/foundations-accessibility-intro%402x.png)

アクセシビリティを考慮して設計することで、より多くのユーザに届くインクルーシブな体験を作成できます。アクセシブルなインターフェイスであれば、ユーザの能力やデバイスの使い方に関係なく、アプリやゲームを楽しめます。アクセシビリティを取り入れることで、誰もが利用しやすい情報や操作が実現します。次のようなインターフェイスはアクセシブルです:

  * **直感的である。** インターフェイスが慣れ親しんだ一貫した操作方法になっており、タスクを明快に実行できます。

  * **認識しやすい。** 複数の方法で情報を伝えています。視覚、聴覚、発話、触覚のどれを使っていても、ユーザがコンテンツを確実に知覚できるようにします。

  * **適応性がある。** システムのアクセシビリティ機能に対応する、ユーザが設定をパーソナライズできるようにするなど、インターフェイスがユーザの希望するデバイスの使い方に合わせて適応します。

アプリのデザインでは、インターフェイスのアクセシビリティを監査してください。[アクセシビリティインスペクタ](/documentation/Accessibility/accessibility-inspector)を使用して、インターフェイスのアクセシビリティの問題をハイライトし、システムのアクセシビリティ機能を使用しているユーザに対してアプリがどのように表示されるかを把握します。また、アクセシビリティ対応機能リストを使用して、App Storeでアプリのアクセシビリティの程度を伝えることもできます。アクセシビリティ機能の対応の評価と表示について詳しくは、App Store Connectヘルプの「[アクセシビリティ対応機能リスト](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels)」を参照してください。

## [視覚](/jp/design/human-interface-guidelines/accessibility#Vision)

![視覚に関するトピックを象徴する5つのシンボルを含む図。テキストサイズ、拡大率、VoiceOver、会話を表すシンボルが含まれています。](https://docs-assets.developer.apple.com/published/b30d1fdd87d5aa7ed3085f0a0ccd61e5/accessibility-vision-section-hero%402x.png)

インターフェイスを使う人は、全盲、色盲、弱視、光過敏であるかもしれません。また、照明条件や画面の明るさがインターフェイスの操作に影響する可能性もあります。

**大きなテキストサイズに対応する。** ユーザがテキストやアイコンのサイズを調整して、判読可能性や視認性を高め、快適に読めるようにします。理想的には、テキストを200%以上（watchOSアプリでは140%以上）拡大できるオプションを用意します。インターフェイスでは、カスタムUIまたはダイナミックタイプを採用することで、フォントサイズの拡大に対応することができます。ダイナミックタイプは、システム全体の設定で、テキストが読みやすいように、サイズを調整できるようにします。詳しいガイダンスは[ダイナミックタイプに対応する](/jp/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)を参照してください。

**カスタム文字サイズには推奨のデフォルトを使用する。** 読みやすさを向上させるため、システムで定義されている文字スタイルのデフォルトと最小のサイズは各プラットフォームによって異なります。カスタムの文字スタイルを使用する場合は、推奨のデフォルトに従ってください。

プラットフォーム| デフォルトのサイズ| 最小サイズ  
---|---|---  
iOS/iPadOS| 17 pt| 11 pt  
macOS| 13 pt| 10 pt  
tvOS| 29 pt| 23 pt  
visionOS| 17 pt| 12 pt  
watchOS| 16 pt| 12 pt  
  
**テキストの読みやすさには、フォントのウェイトも影響することを考慮する。** ウェイトが細いカスタムフォントを使用している場合は、推奨サイズよりも大きくして読みやすくします。詳しいガイダンスは、[タイポグラフィ](/jp/design/human-interface-guidelines/typography)を参照してください。

![四角形のビューの図。「Hello」という単語が含まれており、小さなフォントサイズの太字でフォーマットされています。](https://docs-assets.developer.apple.com/published/80484bda9107b8d01ef5b5a5ae3e6540/accessibility-font-weight-small-bold%402x.png)フォントサイズが小さい場合、太いウェイトを使用すると読みやすくなります。

![四角形のビューの図。「Hello」という単語が含まれており、大きなフォントサイズの細字でフォーマットされています。](https://docs-assets.developer.apple.com/published/d15f7ff9653d9a74ab0ef8b864b42f69/accessibility-font-weight-large-thin%402x.png)細いウェイトを使用する場合は、フォントサイズを大きくすることを検討してください。

**カラーコントラスト比が最低基準を満たすようにする。** アプリのすべての情報が確実に判読可能であるには、前景のテキストやアイコンと背景カラーの十分なコントラストを確保することが重要です。カラーコントラストを測定する際によく使われる基準として、[Web Content Accessibility Guidelines（WCAG）](https://www.w3.org/TR/WCAG/)とAccessible Perceptual Contrast Algorithm（APCA）の2つがあります。基準のコントラスト計算ツールを使用し、UIが許容レベルを満たすようにしてください。[アクセシビリティインスペクタ](/documentation/Accessibility/accessibility-inspector)では、アプリのカラーコントラストが許容範囲に収まっているかどうかを判断するためのガイダンスとして、WCAG Level AAの次の値を使用しています。

テキストサイズ| テキストの線の太さ| 最低コントラスト比  
---|---|---  
17 pt以下| すべて| 4.5:1  
18 pt| すべて| 3:1  
すべて| ボールド| 3:1  
  
アプリがデフォルトでこの最低コントラストを満たしていない場合は、システム設定の「コントラストを上げる」がオンになっているときに、少なくともより高いコントラストのカラースキームを用意します。アプリが[ダークモード](/jp/design/human-interface-guidelines/dark-mode)に対応している場合は、ライトとダークの両方の見た目で最低コントラストを確認します。

![ボタンの図。ボタンのタイトルと背景のコントラスト比が十分ではありません。](https://docs-assets.developer.apple.com/published/35456022505e2a5a6cb412513bac85c3/accessibilty-button-poor-color-contrast%402x.png)カラーコントラストが十分でないボタン

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![ボタンの図。ボタンのタイトルと背景のコントラスト比が十分です。](https://docs-assets.developer.apple.com/published/2a319502f7f963e3f941c1e2d6d7874e/accessibilty-button-good-color-contrast%402x.png)カラーコントラストが十分なボタン

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**システム定義カラーを優先する。** これらのカラーにはアクセシブルなバリアントが存在し、「コントラストを上げる」を有効にした場合やライトのダークの見た目を切り替えた場合など、カラー環境設定を調整したときに自動的に適用されます。ガイダンスは、[カラー](/jp/design/human-interface-guidelines/color)を参照してください。

![明るい背景と暗い背景で、システム定義カラーの赤がどのように表示されるかを示す図。図では、角丸四角形の上に円が配置されています。角丸四角形の左側は明るいカラー、右側は暗いカラーになっています。円の左側は、右側よりもわずかに暗くなっています。](https://docs-assets.developer.apple.com/published/43871e7cf9907fbc19cceb7f37c7d312/accessibility-system-red-ios-default%402x.png)iOSのデフォルトカラー`systemRed`

![明るい背景と暗い背景で、システム定義アクセシビリティ固有カラーの赤がどのように表示されるかを示す図。図では、角丸四角形の上に円が配置されています。角丸四角形の左側は明るいカラー、右側は暗いカラーになっています。円の左側は、右側よりもかなり暗くなっています。](https://docs-assets.developer.apple.com/published/903eccfee98cfa852c318e9785f7e334/accessibility-system-red-ios-accessible%402x.png)iOSのアクセシブルなカラー`systemRed`

**カラーだけで情報を伝えない。** 特定のカラーや色合いを見分けるのが難しい人もいます。例えば色盲の人は、赤と緑、青とオレンジなどのペアを見分けるのが特に難しいかもしれません。ユーザが機能や状態の変化の違いを認識できるようにするため、カラーだけでなく、形状やアイコンを変えるなど、視覚的なインジケータを提供してください。ユーザがグラフの色やゲームキャラクターなどのカラースキームをカスタマイズして、自分にとって使いやすいインターフェイスにパーソナライズできるようにすることを検討してください。

![緑の円が赤い円の左側にある図。](https://docs-assets.developer.apple.com/published/5d62d6f6c6ff1563d80847b3b29e2125/accessibility-differentiate-with-shapes-incorrect%402x.png)赤と緑の色盲がある人には、同じに見える可能性があります。

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![チェックマークを含む緑の円がバツ印を含む赤い八角形の左側にある図。](https://docs-assets.developer.apple.com/published/e13c9c34a780c2d2ab0e614f55a3e73e/accessibility-differentiate-with-shapes-correct%402x.png)視覚的なインジケータとカラーの両方により、見分けやすくなっています。

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**VoiceOver向けにアプリのインターフェイスやコンテンツを説明する。** VoiceOverは画面読み上げ機能です。VoiceOverを使うと、画面を見ずにアプリのインターフェイスを使うことができます。詳しいガイダンスは、[VoiceOver](/jp/design/human-interface-guidelines/voiceover)を参照してください。

## [聴覚](/jp/design/human-interface-guidelines/accessibility#Hearing)

![聴覚に関するトピックを象徴する5つのシンボルを含む図。サウンド、波形、クローズドキャプションを表すシンボルが含まれています。](https://docs-assets.developer.apple.com/published/eef3040be22f7aa6b10dc45b2918f9f8/accessibility-hearing-section-hero%402x.png)

インターフェイスを使う人は、耳が聞こえなかったり、難聴だったりするかもしれません。騒がしい場所や公共の場所にいる可能性もあります。

**テキストベースの方法でオーディオやビデオを楽しめるようにする。** アプリやゲームの会話や重要な情報をオーディオだけで伝えないことが重要です。状況に応じて、別のテキストベースの方法でメディアを体験できるようにし、そのテキストを視覚的に提示する方法をカスタマイズできるようにしてください:

  * **キャプション** は、ビデオや音声専用コンテンツの音声情報をテキストで伝える機能です。キャプションは、ゲームのカットシーンやビデオクリップなど、テキストがメディアとライブで同期するシナリオに最適です。

  * **字幕** は、画面上の台詞を、ユーザが自分の優先する言語でリアルタイムに読めるようにします。字幕は、テレビ番組や映画に最適です。

  * **バリアフリー音声ガイド** は、ビデオのメイン音声が自然に休止している間に挿入され、視覚のみで提示される重要な情報の音声によるナレーションです。

  * **文字起こし** は、ビデオを完全にテキストで記述したもので、聴覚と視覚両方の情報をカバーします。文字起こしはポッドキャストやオーディオブックなどの長編メディアに最適で、ユーザはコンテンツ全体を確認したり、メディアの再生中に文字起こしをハイライトしたりできます。

デベロッパ向けのガイダンスは、[字幕および代替オーディオトラックの選択](/documentation/AVFoundation/selecting-subtitles-and-alternative-audio-tracks)を参照してください。

**オーディオキューと合わせて触覚フィードバックを使用する。** 成功を表すチャイム音、エラーを表す音、ゲームのフィードバックなどのオーディオキューによってインターフェイスで情報を伝える場合は、オーディオを認識できない人やオーディオをオフにしている人に向けて、サウンドに合った触覚フィードバックも行うことを検討してください。iOSおよびiPadOSで[ミュージックの触覚](/documentation/MediaAccessibility/music-haptics)や[オーディオグラフ](/documentation/Accessibility/audio-graphs)を使い、ミュージックやインフォグラフィックを振動と模様で体験することもできます。ガイダンスは、[触覚フィードバックの提供](/jp/design/human-interface-guidelines/playing-haptics)を参照してください。

![iPhoneデバイスの図。デバイスのミュージック再生に合わせて振動しています。](https://docs-assets.developer.apple.com/published/1bf9d6ae5c3586a5163ce6abf0cabb95/accessibility-haptic-audio-combo%402x.png)

**オーディオキューを視覚的なフィードバックで補強する。** この点は、重要なコンテンツが画面外で発生することがあるゲームや空間アプリでは特に重要です。オーディオを使用してユーザに特定のアクションを指示する場合は、ユーザに操作を行ってほしい場所を示す視覚的インジケータも追加してください。

## [身体機能](/jp/design/human-interface-guidelines/accessibility#Mobility)

![身体機能に関するトピックを象徴する5つのシンボルを含む図。キーボード、移動、タッチを表すシンボルが含まれています。](https://docs-assets.developer.apple.com/published/f8e9d74dc994111ba0ee7fa436fc2fc1/accessibility-mobility-section-hero%402x.png)

器用さや身体機能に限界がある人でも、快適にインターフェイスを体験できるようにしてください。

**十分なサイズのコントロールを提供する。** コントロールが小さすぎると、操作したり選択したりするのが難しくなります。あらゆる人がコントロールやメニューを快適にタップまたはクリックできるように、各プラットフォームの推奨の最小コントロールサイズに従ってください。

プラットフォーム| デフォルトのコントロールサイズ| 最小コントロールサイズ  
---|---|---  
iOS/iPadOS| 44x44 pt| 28x28 pt  
macOS| 28x28 pt| 20x20 pt  
tvOS| 66x66 pt| 56x56 pt  
visionOS| 60x60 pt| 28x28 pt  
watchOS| 44x44 pt| 28x28 pt  
  
**コントロール間のスペースもサイズと同様に重視する。** 要素間に十分なパディングを設け、間違ったコントロールがタップされる確率を減らします。通常は、要素の周囲にベゼルを含めて12ポイントほどのパディングを追加するとよいでしょう。ベゼルがない要素では、要素の目に見える境界の周囲に24ポイントほどのパディングを追加するとよいでしょう。

![早戻し、再生、早送りの3つのボタンを示す図。ボタンの間に十分なパディングがありません。](https://docs-assets.developer.apple.com/published/4148fe218b3f50b66d64eeda288de5be/accessibility-controls-spacing-incorrect%402x.png)パディングが十分でない要素

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![早戻し、再生、早送りの3つのボタンを示す図。ボタンの間にスペースがあり、十分なパディングが設けられています。](https://docs-assets.developer.apple.com/published/98bc500a0a2cf15620b972de1fcce3b3/accessibility-controls-spacing-correct%402x.png)パディングが十分な要素

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**よく使う操作を簡単なジェスチャで行えるようにする。** 障がいの有無にかかわらず、複雑なジェスチャを行うのは難しいことです。アプリやゲームで頻繁に行う操作は、できる限り簡単なジェスチャで行えるようにします。複数の指や手を使ったカスタムのジェスチャは避け、繰り返し行うアクションが快適で覚えやすいものになるようにしてください。

**ジェスチャの代替手段を提供する。** UIの主要機能は、複数のタイプの身体的操作で利用できるようにしてください。器用さに限界がある人は、快適にジェスチャを行えない場合があります。そのため、画面上で同じ結果を実現する方法を提供します。例えば、スワイプジェスチャを使用してビューを閉じる場合は、タップや補助装置で利用できるボタンも作ります。

![編集モードのテーブルビューの図。テーブルの列には削除ボタンが含まれています。](https://docs-assets.developer.apple.com/published/9fc10b042706da8343f2421de6d9b985/accessibility-tap-to-delete%402x.png)編集とタップで削除

![テーブルビューの図。テーブルのいずれかの列を左にスワイプすると、削除ボタンが表示されます。](https://docs-assets.developer.apple.com/published/31bb8b3cc6096522c047c0fd5243fcff/accessibility-swipe-to-delete%402x.png)スワイプして削除

**音声コマンドでの指示や音声での情報の入力に対応する。** 音声コマンドを使用すると、コマンドを話すだけでデバイスを操作できます。ジェスチャを実行する、画面要素を操作する、テキストを入力したり編集したりするなどの操作ができます。スムーズな体験を実現できるように、インターフェイス要素に適切なラベルを付けてください。デベロッパ向けのガイダンスは、[音声コマンド](/documentation/Accessibility/voice-control)を参照してください。

**Siriやショートカットを組み込んで声だけでタスクを実行できるようにする。** Siriやショートカットに対応したアプリでは、何度も定期的に行う必要がある重要なタスクを自動化できます。こういったタスクは、Siri、iPhoneまたはApple Watchのアクションボタン、ホーム画面やコントロールセンターのショートカットから開始できます。ガイダンスは[Siri](/jp/design/human-interface-guidelines/siri)を参照してください。

**身体機能関連の操作補助技術に対応する。**[VoiceOver](/jp/design/human-interface-guidelines/voiceover)、AssistiveTouch、フルキーボードアクセス、ポインタコントロール、[スイッチコントロール](/documentation/Accessibility/switch-control)などの機能は、身体機能に制約があってデバイスを操作しにくい方のための代替手段を提供します。優れた体験を提供するため、テストを行い、アプリやゲームがこういった技術に対応していることやインターフェイス要素に適切なラベルが付いていることを確認してください。詳しい情報は、[アプリでアクセシビリティテストを行う](/documentation/Accessibility/performing-accessibility-testing-for-your-app)を参照してください。

## [スピーチ](/jp/design/human-interface-guidelines/accessibility#Speech)

![スピーチに関するトピックを象徴する5つのシンボルを含む図。波形、スピーチを表すシンボルが含まれています。](https://docs-assets.developer.apple.com/published/62f06a887d774ec29a27ce2be6d30444/accessibility-speech-section-hero%402x.png)

Appleのアクセシビリティ機能は、言語障がいがある方や、デバイスを使用したコミュニケーションにおいてテキストベースのやりとりの方が効率的である方をサポートします。

**ユーザがキーボードでアプリに移動して操作できるようにする。** ユーザがフルキーボードアクセスをオンにすると、物理キーボードを使用してアプリを操作できます。システムでは、アクセシビリティのキーボードショートカットに加えて、多くのユーザが頻繁に使用する[キーボードショートカット](https://support.apple.com/en-us/102650)を数多く定義しています。システムで定義されているキーボードショートカットを上書きするのは避け、アプリを評価してフルキーボードアクセスが適切に動作するようにします。追加のガイダンスは、[キーボード](/jp/design/human-interface-guidelines/keyboards)を参照してください。デベロッパ向けのガイダンスは、[iOSアプリでフルキーボードアクセスに対応する](https://developer.apple.com/videos/play/wwdc2021/10120)を参照してください。

**スイッチコントロールに対応する。** スイッチコントロールは支援技術の1つです。別売のハードウェア、ゲームコントローラ、クリックやポップなどのサウンドを使ってデバイスを制御できます。アプリやゲームがスイッチコントロールによる操作に対応している場合、ユーザは選択、タップ、入力、描画などのアクションを実行できます。デベロッパ向けのガイダンスは、[スイッチコントロール](/documentation/Accessibility/switch-control)を参照してください。

## [認知](/jp/design/human-interface-guidelines/accessibility#Cognitive)

![認知に関するトピックを象徴する5つのシンボルを含む図。ミュージック、セキュリティ、情報階層を表すシンボルが含まれています。](https://docs-assets.developer.apple.com/published/0d837305d3c06f6ba0199cf2764df3fd/accessibility-cognitive-section-hero%402x.png)

アプリやゲームをできる限りシンプルにすることは、すべての人のメリットにつながります。

**アクションはシンプルで直感的なものにする。** 覚えやすい一貫した操作方法でインターフェイスを移動できるようにします。学習して覚えなければならないカスタムのジェスチャを作成するよりも、すでにユーザが慣れ親しんでいるシステムのジェスチャや動作を優先してください。

**時間制限のあるインターフェイス要素は極力使わない。** タイマーによってビューやコントロールを自動で閉じるようにすると、情報処理に時間が必要な人や、操作補助技術を使用しているためインターフェイスの移動に時間がかかる人にとって問題になる場合があります。明示的なアクションで閉じるビューを優先してください。

**ゲームの難易度調整の提供を検討する。** ゲームのプレイ方法や楽しみ方は人それぞれです。さまざまな認知能力に対応するため、ゲームの難易度をカスタマイズできる機能の追加を検討してください。ユーザがレベルクリア条件の緩和、反応時間の調整、制御支援の有効化などをできるオプションを用意します。

**ユーザがオーディオやビデオの再生をコントロールできるようにする。** 開始と停止のコントロールを設けずにオーディオやビデオのコンテンツを自動再生しないようにします。これらのコントロールを見つけやすい場所に配置し、簡単に操作できるようにしてください。また、すべてのオーディオやビデオの自動再生を無効にするグローバル設定について検討してください。デベロッパ向けのガイダンスは、[アニメーション画像](/documentation/Accessibility/animated-images)および[`isVideoAutoplayEnabled`](/documentation/UIKit/UIAccessibility/isVideoAutoplayEnabled)を参照してください。

**ビデオ再生時の点滅する光を無効化できるようにする。** メディアを視聴する際に、明るい光や頻繁に点滅する光を好まない人もいます。「刺激的な光の点滅を検知時に暗くする」設定を利用すると、点滅する光がメディアに含まれている場合に、それを計算して軽減したり、ユーザに通知したりできます。ビデオを再生できるアプリでは、「刺激的な光の点滅を検知時に暗くする」設定に適切に対応してください。デベロッパ向けのガイダンスは、[光の点滅](/documentation/MediaAccessibility/flashing-lights)を参照してください。

**動きの速いアニメーションや点滅するアニメーションに注意する。** こういった効果を多用しすぎると、邪魔になったり、めまいを引き起こしたりすることがあります。場合によってはてんかんの発作が起きる場合もあります。こういった症状が現れやすい人は、「視差効果を減らす」アクセシビリティ設定をオンにすることができます。アプリやゲームでこの設定が有効な場合、ズーム、拡大/縮小、周辺の動きなどの自動的に繰り返されるアニメーションを軽減してください。動きを軽減するその他のベストプラクティスには、以下のようなものがあります:

  * スプリング効果を制限してアニメーションのバウンスエフェクトを減らす

  * ユーザのジェスチャでアニメーションを直接トラッキングする

  * Z軸レイヤーで奥行きを変化させるアニメーションを避ける

  * X軸、Y軸、Z軸の移動をフェードに置き換えて動きをなくす

  * アニメーションでボケやブレなどの効果を使用しない

**アシスティブアクセス用にアプリのUIを最適化する。** アシスティブアクセスは、認知障がいを持つユーザがアプリの簡略版を使えるようにする、iOSおよびiPadOSのアクセシビリティ機能の1つです。アシスティブアクセスでは、カメラアプリの次のレイアウトのように、アプリで認知負荷を軽減するデフォルトのレイアウトとコントロールの表示を設定します。

![アシスティブアクセスでのカメラアプリのスクリーンショット。「写真」、「ビデオ」、および「戻る」の3つの大きなボタンのあるインターフェイスが表示されています。](https://docs-assets.developer.apple.com/published/60cd8115bd31d4da6198d71855a14e62/accessibility-assistive-access-camera%402x.png)

![アシスティブアクセスで写真の画面を開いたカメラアプリのスクリーンショット。「写真を撮る」および「戻る」の2つの大きなボタンのあるインターフェイスが表示されています。](https://docs-assets.developer.apple.com/published/5bb90e7b610e7f616b156c1d151433d5/accessibility-assistive-access-camera-photo-mode%402x.png)

このモード用にアプリを最適化するには、「アシスティブアクセス」がオンになっているときは以下のガイドラインに従ってください:

  * アプリのコア機能を特定し、重要でないワークフローやUI要素は削除することを検討します。

  * 複数のステップからなるワークフローは分割し、ユーザが1つの画面で1つの操作に集中できるようにします。

  * ファイルの削除など、元に戻すことが困難なアクションを実行する場合は、必ず2回確認します。

デベロッパ向けのガイダンスは、[アシスティブアクセス](/documentation/Accessibility/assistive-access)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/accessibility#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、watchOSに追加の考慮事項はありません。_

### [visionOS](/jp/design/human-interface-guidelines/accessibility#visionOS)

visionOSでは、頭と手によるポインタコントロールや拡大/縮小機能などのさまざまなアクセシビリティ機能が提供され、自分の置かれた状況に合わせて周辺の環境を体験できるようになっています。

以下のカスタムコントロールを使用できます 

このビデオコンテンツの説明: アプリのvisionOSウインドウ内でコンテンツを操作するためにポインタコントロールを使っているユーザの手の録画。ユーザの手からポインタまで線が延びています。ユーザが手を動かすと、視野の中での線の位置が変わります。 

再生 

以下のカスタムコントロールを使用できます 

このビデオコンテンツの説明: アプリのvisionOSウインドウ内でコンテンツを操作するためにポインタコントロールを使っているユーザの録画。ユーザは映っていません。ポインタのみが見えています。ポインタは視野の中央にあり、ユーザは頭を動かしてポインタをコンテンツの上に移動します。 

再生 

![visionOSのアプリのウインドウのスクリーンショット。ズームレンズがウインドウのある部分の上にあり、レンズの下にあるコンテンツを拡大表示しています。](https://docs-assets.developer.apple.com/published/087dd22d68c54c95cd70008020f6dc1e/visionos-accessibility-zoom-lens%402x.png)

**快適性を優先する。** visionOSの没入的な性質上、インターフェイス、アニメーション、インタラクションによって、乗り物酔いや視覚的または人間工学的な不快感が発生する確率が高まります。最大限に快適な体験を実現するため、以下のヒントについて考慮してください:

  * インターフェイス要素は視野に含めるようにします。首に負担がかかる垂直レイアウトよりも、水平レイアウトを優先します。また、連続して別の場所に注意を向けることを求めないようにします。

  * 特に周辺視野において、アニメーションするオブジェクトの速度や明るさを抑えるようにします。

  * カメラやビデオの移動を抑え、何の操作も行わずに周囲の世界が動いているように感じられる状況を避けます。

  * 装着者の頭にコンテンツをアンカーしないようにします。これを行うと、引っかかっている感覚や閉じ込められた感覚につながるだけでなく、ポインタコントロールなどの操作補助技術が利用できなくなります。

  * 大きなジェスチャを繰り返し使うことが求められる場面をできる限り減らします。こういったジェスチャは面倒で、周囲の環境によっては行うのが難しい場合があります。

その他のガイダンスは、[アクセシブルな空間体験を作成する](https://developer.apple.com/videos/play/wwdc2023/10034)および[視覚と運動に関する設計上の考慮事項](https://developer.apple.com/videos/play/wwdc2023/10078)を参照してください。

## [リソース](/jp/design/human-interface-guidelines/accessibility#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/accessibility#Related)

[インクルージョン](/jp/design/human-interface-guidelines/inclusion)

[タイポグラフィ](/jp/design/human-interface-guidelines/typography)

[VoiceOver](/jp/design/human-interface-guidelines/voiceover)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/accessibility#Developer-documentation)

[アクセシビリティ対応のアプリを開発する](https://developer.apple.com/accessibility/)

[Accessibilityフレームワーク](/documentation/Accessibility)

[アクセシビリティ対応機能リストの概要](https://devcms.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels)

#### [ビデオ](/jp/design/human-interface-guidelines/accessibility#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/316)

[](https://developer.apple.com/videos/play/wwdc2025/224)

[](https://developer.apple.com/videos/play/wwdc2024/10073)

## [変更履歴](/jp/design/human-interface-guidelines/accessibility#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| アシスティブアクセス、スイッチコントロール、およびアクセシビリティ対応機能リストに関するガイダンスとリンクを追加。  
2025年3月07日| すべてのガイダンスの追加と改訂。ダイナミックタイプのガイダンスをタイポグラフィのページに、VoiceOverのガイダンスを新しいVoiceOverのページに移動。  
2024年6月10日| ダイナミックタイプに対応するためのAppleのUnityプラグインへのリンクを追加しました。  
2023年12月05日| visionOSのズームレンズアートワークを更新。  
2023年6月21日| visionOSのガイダンスを追加するために更新。
