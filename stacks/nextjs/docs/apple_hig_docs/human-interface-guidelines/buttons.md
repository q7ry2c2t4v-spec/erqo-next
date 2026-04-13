# ボタン

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/buttons

2025年12月16日

Liquid Glassに関するガイダンスを更新。 

# ボタン

ボタンは即座にアクションを開始します。

![水平に並んだ2つの図案化されたボタン。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/1a0f0641d6f2938b5daf1c8104bdfae7/components-buttons-intro%402x.png)

多くの用途に利用でき、カスタマイズ性の高いボタンは、ユーザがタスクの実行に日常的に使うシンプルなコンポーネントです。一般的にボタンの機能は、以下の3つの属性から明確に理解できます。

  * **スタイル:** サイズ、色、形状に基づく視覚的なスタイルです。

  * **コンテンツ:** ボタンに表示されるシンボル（またはアイコン）、テキストラベル、またはその両方からボタンの目的が分かります。

  * **役割:** ボタンの意味を表すシステムで定義された役割で、見た目に影響する場合があります。

ボタンに似ているが、特定のユースケースに合わせて外見や動作が明確に区別されているコンポーネントも数多く存在します。[トグル](/jp/design/human-interface-guidelines/toggles)、[ポップアップボタン](/jp/design/human-interface-guidelines/pop-up-buttons)、[セグメントコントロール](/jp/design/human-interface-guidelines/segmented-controls)などです。

## [ベストプラクティス](/jp/design/human-interface-guidelines/buttons#Best-practices)

すぐに認識できる分かりやすいボタンを配置すれば、多くのユーザに、直感的に使える優れた設計のアプリであると評価してもらえます。

**ユーザが使いやすいボタンにする。** ボタンをその周囲のコンポーネントやコンテンツから容易に区別できるように、ボタンの周りに十分なスペースを取ることは非常に重要です。ボタン周りのスペースは、ユーザがどの入力方法を使用するかにかかわらず、ボタンを選択したり有効化したりする操作を容易にするためにも重要です。指やポインタ、視線、リモコンなど、どの入力方法でもボタンを簡単に選択できるようにするには、基本的にボタンのヒット領域を44x44 pt以上（visionOSの場合は60x60 pt以上）にする必要があります。

**カスタムボタンには押されている状態も必ず用意する。** 押されている状態がないと、ボタンが応答していないように感じ、入力が受け付けられたかどうかユーザが不安に感じてしまいます。

## [スタイル](/jp/design/human-interface-guidelines/buttons#Style)

システムには、カスタマイズに対応するさまざまなスタイルのボタンがあります。これらのボタンは、操作の状態、アクセシビリティ対応、見た目の適応といった機能を内蔵しています。アプリのアクションの階層構造をユーザが簡単に把握できるように、プラットフォームに合わせてさまざまなスタイルが定義されています。

**基本的に、ビューの中で最もよく使われるであろうアクションのボタンには目立つスタイルを使う。** 特定のボタンにユーザの注意を向けるには、目立つボタンスタイルを使用し、ボタンの背景にアクセントカラーを適用します。通常、カラーを使うとボタンを見分けやすくなり、よく使用するアクションをユーザがすぐに見つけるのに役立ちます。目立たせるボタンの数は、1つのビューにつき2つまでにしてください。目立つボタンが多すぎるとユーザの認知負荷が増えて、選択前のオプションの検討に余計に時間がかかってしまいます。

**複数の選択肢の中で推奨するものを視覚的に差別化する場合は、サイズではなくスタイルを使用する。** 複数の選択肢を提示する際に同じサイズのボタンを使うと、それらが一まとまりの選択肢であることが分かります。逆に、サイズの異なるボタンを互いに近づけて配置すると、インターフェイスが分かりにくくなり、一貫性がなくなります。推奨される選択肢や最もよく使われる選択肢を強調したい場合は、その選択肢に目立つボタンスタイルを適用し、ほかの選択肢にはそれよりも目立たないスタイルを適用します。

**ボタンのラベルとコンテンツレイヤーの背景に似たカラーを適用しない。** アプリのコンテンツレイヤーにすでに明るくカラフルなコンテンツがある場合、ボタンのラベルにはできるだけデフォルトのモノクロの見た目を使用してください。Liquid Glassのコントロールのラベルと、コントロールの背後のコンテンツに似た色を使用すると、色の区別がつきにくくなる可能性があります。詳しいガイダンスは[Liquid Glassカラー](/jp/design/human-interface-guidelines/color#Liquid-Glass-color)を参照してください。

## [コンテンツ](/jp/design/human-interface-guidelines/buttons#Content)

**目的が明確に伝わるボタンにする。** プラットフォームによりますが、ボタンが実行する処理をユーザが理解できるように、ボタンにはシンボル（またはアイコン）、テキストラベル、またはその両方を含めることができます。

備考

macOSとvisionOSでは、ユーザがボタンに短時間ポインタを合わせると、ツールチップが表示されます。ツールチップの内容は、ボタンの機能を説明する簡潔な語句です。ガイダンスは[ヘルプの提供](/jp/design/human-interface-guidelines/offering-help)を参照してください。

**慣れ親しんだアクションを見慣れたアイコンと関連付ける。** 例えば、`square.and.arrow.up`シンボルを含むボタンであれば、ユーザはそこから共有関連のアクティビティが実行されると予想できます。ボタンでアイコンを使うのが適切な場合は、なるべく既存またはカスタマイズした[シンボル](/jp/design/human-interface-guidelines/sf-symbols)を使用してください。一般的なアクションを表すシンボルのリストは、[標準のアイコン](/jp/design/human-interface-guidelines/icons#Standard-icons)を参照してください。

**アイコンより短いラベルの方がもっと明確に意図を伝達できる場合は、テキストを使う。** テキストを使用する場合は、ボタンによって何が起きるのかを簡潔に説明する文言にします。[タイトルとしてふさわしいスタイル](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64)を使用し、ラベルにはボタンのアクションを示す動詞を含めることを検討してください。例えば、商品をショッピングカートに追加するボタンなら、「カートに追加」というラベルにします。

## [役割](/jp/design/human-interface-guidelines/buttons#Role)

システムのボタンには、以下の役割のいずれかを割り当てることができます。

  * **通常:** 特別な意味はありません。

  * **プライマリ:** ユーザが選択する可能性が最も高いデフォルトのボタンです。

  * **キャンセル:** 現在のアクションをキャンセルするボタンです。

  * **破壊的:** データの破壊につながるアクションを実行するボタンです。

ボタンの役割によっては、ボタンの見た目に追加の影響が及びます。例えば、プライマリボタンにはアプリのアクセントカラーが、破壊的なボタンにはシステムの赤色が使用される場合があります。

![「プライマリ」、「破壊的」、および「キャンセル」というラベルが付いた3つのシステムのボタンがあるサンプルのアラート。プライマリボタンには青のアクセントカラー、破壊的ボタンにはシステムの赤色のテキストが使用され、キャンセルボタンは標準的なボタンとして表示されます。](https://docs-assets.developer.apple.com/published/05c9bf6d2e1e8f9a9843a67228d9c893/buttons-roles-alert%402x.png)

**ユーザが選択する可能性が最も高いボタンにはプライマリの役割を割り当てる。** プライマリボタンがReturnキーに反応するデバイスでは、選択される可能性が高い項目の選択操作が素早く簡単になります。さらに、ボタンが[シート](/jp/design/human-interface-guidelines/sheets)、編集可能なビュー、[アラート](/jp/design/human-interface-guidelines/alerts)などの一時的なビューに表示される場合、そのボタンにプライマリの役割を割り当てると、Returnキーの押下で自動的にビューが閉じます。

**最も選択される可能性が高くても破壊的なアクションを実行するボタンにはプライマリの役割を割り当てない。** プライマリのボタンは視覚的に目立つため、ユーザがラベルを読まずに押してしまう可能性があります。プライマリの役割は非破壊的なボタンに割り当て、ユーザがコンテンツを失わないようにしてください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/buttons#Platform-considerations)

 _tvOSに追加の考慮事項はありません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/buttons#iOS-iPadOS)

**すぐに完了しないアクションのフィードバックを提供する必要がある場合は、アクティビティインジケータを表示するように設定する。** ボタン内にアクティビティインジケータを表示すると、ユーザインターフェイス領域を節約でき、時間がかかる理由を明確に伝えることもできます。処理内容を明らかにするために、アクティビティインジケータと合わせて、ボタンに異なるラベルを表示することもできます。例えば、アクティビティインジケータが表示されている間は、「チェックアウト」というラベルを「チェックアウト中…」に変更します。ボタンのクリックまたはタップ後の処理に時間がかかっている場合、このように設定したボタンでは、アクティビティインジケータが元のラベルまたは変更されたラベルの横に表示され、ボタンに画像がある場合はそれが非表示になります。

![「チェックアウト」というラベルが付いたボタンの図。](https://docs-assets.developer.apple.com/published/d474f4577308896b005d8b2b6523357b/button-activity-indicator-hidden%402x.png)

![「チェックアウト中」というラベルが付いたボタンの図。ラベルの先頭側にアクティビティインジケータがあります。](https://docs-assets.developer.apple.com/published/68d69644ecde19de5e4f471c490a43f0/button-activity-indicator-visible%402x.png)

### [macOS](/jp/design/human-interface-guidelines/buttons#macOS)

macOSには、ほかにはない特殊なタイプのボタンがいくつか存在します。

#### [プッシュボタン](/jp/design/human-interface-guidelines/buttons#Push-buttons)

macOSの標準のボタンタイプは、 _プッシュボタン_ と呼ばれます。プッシュボタンには、テキスト、シンボル、アイコン、画像、またはテキストと画像コンテンツの組み合わせを表示できます。プッシュボタンはビューのデフォルトのボタンとして動作し、色を付けることもできます。

**高さが可変のプッシュボタンは、縦に長いコンテンツや高さが可変のコンテンツを表示する必要がある場合のみ使用する。** 高さが可変のボタンは、通常のプッシュボタンと同じ設定に対応し、同じ角丸の半径とコンテンツの余白が使用されます。これは、インターフェイスのほかのボタンとの見た目の一貫性を保つためです。2行のテキストや縦に長いアイコンを含むボタンを表示する必要がある場合は、高さが可変のボタンを使用します。それ以外の場合は、標準のプッシュボタンを使用します。デベロッパ向けのガイダンスは、[`NSButton.BezelStyle.flexiblePush`](/documentation/AppKit/NSButton/BezelStyle-swift.enum/flexiblePush)を参照してください。

**プッシュボタンで別のウインドウ、ビュー、アプリを開く場合は、タイトルの末尾に省略記号を追加する。** コントロールの選択後にユーザが情報をさらに入力する場合は、当該コントロールのタイトルに省略記号が付けるのが、システム全体に適用される原則です。例えば、Safariの「設定」の「自動入力」パネルの「編集」ボタンを選択すると、自動入力の値を変更する別のビューが開くので、ボタンのタイトルに省略記号が付加されています。

**スプリングローディングへの対応を検討する。** Magic Trackpadが搭載されたシステムでは、選択した項目をドラッグしてドロップせずに強めのクリックをすると、 _スプリングローディング_ でボタンを作動させることができます。強めのクリックをしてからドラッグを続けることで、追加のアクションを実行することもできます。

#### [正方形のボタン](/jp/design/human-interface-guidelines/buttons#Square-buttons)

 _正方形のボタン_ は、 _グラディエントボタン_ とも呼ばれ、テーブルの行の追加や削除など、ビューに関連するアクションを開始する際に使用します。

正方形のボタンには、テキストではなくシンボルかアイコンが含まれており、プッシュボタン、トグル、ポップアップボタンのような動作を設定できます。関連するビューのすぐそば（通常は内部か下）にボタンが表示されるので、ユーザはボタンがどのビューに影響するかが分かります。

**正方形のボタンはウインドウフレームではなくビューで使用する。** 正方形のボタンはツールバーやステータスバーで使うものではありません。[ツールバー](https://developer.apple.com/jp/design/human-interface-guidelines/toolbars)にボタンを表示する必要がある場合は、ツールバーの項目を使用してください。

**正方形のボタンにはなるべくシンボルを使用する。**[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)には、デフォルトの状態で適切な色が割り当てられた、さまざまなシンボルが用意されています。これらのシンボルは、ユーザの操作に反応して自動的に適切な色に変わります。

**ラベルを使って正方形のボタンを説明しない。** 正方形のボタンは特定のビューと密接に結びついているため、基本的に説明文がなくても目的がはっきり分かります。

デベロッパ向けのガイダンスは、[`NSButton.BezelStyle.smallSquare`](/documentation/AppKit/NSButton/BezelStyle-swift.enum/smallSquare)を参照してください。

#### [ヘルプボタン](/jp/design/human-interface-guidelines/buttons#Help-buttons)

 _ヘルプボタン_ はビューの中に表示され、アプリ特有のヘルプ文書が開きます。

ヘルプボタンは疑問符が含まれる丸いボタンで、サイズは常に一定です。ヘルプ文書作成のガイダンスは[ヘルプの提供](/jp/design/human-interface-guidelines/offering-help)を参照してください。

**ヘルプ文書の表示にはシステムが提供するヘルプボタンを使用する。** ユーザは標準のヘルプボタンの見た目に慣れており、それを選択するとヘルプコンテンツが開くことを知っています。

**可能な場合は、現在のコンテキストに関連するヘルプトピックを開く。** 例えば、「メール」の設定の「ルール」パネルのヘルプボタンでは、メールユーザガイドのルールの設定を変更する方法を説明したヘルプトピックが開きます。ヘルプボタンが選択されたときに、現在のコンテキストに直接対応する具体的なヘルプトピックがない場合は、アプリのヘルプ文書のトップレベルが表示されます。

**ヘルプボタンはウインドウ1つにつき1つだけにする。** 同じ状況で複数のヘルプボタンが表示されると、クリックしたときの結果が予測しづらくなります。

**ヘルプボタンは期待される場所に配置する。** 以下の場所を参考にしてください。

ビューのスタイル| ヘルプボタンの場所  
---|---  
閉じるボタン（「OK」や「キャンセル」など）があるダイアログ| 閉じるボタンの反対側の下の隅で、ボタンと縦に揃える  
閉じるボタンのないダイアログ| 左下隅または右下隅  
設定ウインドウまたはパネル| 左下隅または右下隅  
  
**ヘルプボタンはウインドウフレームではなくビューで使用する。** 例えば、ヘルプボタンをツールバーやステータスバーに配置しないようにします。

**ヘルプボタンを説明するテキストを表示しない。** ユーザはヘルプボタンの動作を知っています。追加の説明テキストは不要です。

#### [画像ボタン](/jp/design/human-interface-guidelines/buttons#Image-buttons)

 _画像ボタン_ はビューに配置します。画像、シンボル、アイコンを表示できます。画像ボタンには、プッシュボタン、トグル、ポップアップボタンのような動作を設定できます。

**画像ボタンはウインドウフレームではなくビューで使用する。** 例えば、画像ボタンをツールバーやステータスバーに配置しないようにします。ツールバーで画像をボタンとして使用する必要がある場合は、ツールバーの項目を使用します。[ツールバー](/jp/design/human-interface-guidelines/toolbars)を参照してください。

**画像の端とボタンの端との間に約10ピクセルの余白を設ける。** 画像ボタンの端には、見えていなくてもクリック可能な領域を定義できます。この領域があるので、厳密に画像内をクリックしていなくても、クリックが検知されます。基本的に、システムが提供する境界線は画像ボタンには含めません。デベロッパ向けのガイダンスは、[`isBordered`](/documentation/AppKit/NSButton/isBordered)を参照してください。

**ラベルを表示する必要がある場合は、画像ボタンの下に配置する。** 関連のガイダンスは[ラベル](/jp/design/human-interface-guidelines/labels)を参照してください。

### [visionOS](/jp/design/human-interface-guidelines/buttons#visionOS)

visionOSのボタンは通常、ユーザにとって見やすくなるように視認できるバックグラウンドを持ち、ボタンへの操作に対してサウンドでフィードバックを返します。

以下のカスタムコントロールを使用できます 

このビデオコンテンツの説明: 録画。visionOSでウインドウの上部が表示されています。ウインドウには複数のボタンがあり、そのうちの「さらに表示」ボタンにホバーエフェクトが適用されます。そのボタンが選択され、追加のオプションを含むメニューが表示されます。 

再生 

visionOSには、標準ボタンの形状が3つあります。通常は、アイコンのみのボタンには[`circle`](/documentation/SwiftUI/ButtonBorderShape/circle)の形状を使い、テキストのみのボタンには[`roundedRectangle`](/documentation/SwiftUI/ButtonBorderShape/roundedRectangle)または[`capsule`](/documentation/SwiftUI/ButtonBorderShape/capsule)の形状を使います。また、アイコンとテキストの両方を含むボタンにはカプセル型の形状を使います。

visionOSのボタンでは、さまざまな視覚スタイルを使って、4つの操作状態を伝達します。

![円形ボタンの画像。角丸正方形のアイコンが中にあります。ボタンの背景は暗く、点線の輪郭線は白です。](https://docs-assets.developer.apple.com/published/aed0b1c313448f088dd1ee24663db11e/visionos-button-state-idle%402x.png)待機中

![円形ボタンの画像。角丸正方形のアイコンが中にあります。ボタンの背景は中間の暗さで、輪郭線は白です。](https://docs-assets.developer.apple.com/published/29d708fd7985184cbee9d90d7684da92/visionos-button-state-hover%402x.png)ポイント（Hover）

![円形ボタンの画像。角丸正方形のアイコンが中にあります。ボタンの背景は白で、輪郭線は黒です。](https://docs-assets.developer.apple.com/published/0b94e710605235dfca19ef853499cf26/visionos-button-state-selected%402x.png)選択済み

![円形ボタンの画像。角丸正方形のアイコンが中にあります。ボタンの背景は非常に暗く、輪郭線は明るいです。](https://docs-assets.developer.apple.com/published/737120252765e5427161af32bb17e7fb/visionos-button-state-unavailable%402x.png)使用不可

注意

visionOSでは、ボタンはカスタムのホバーエフェクトに対応していません。

ボタンでは、上に示した4つの状態に加えて、ユーザがボタンを見つめたときにツールチップを表示することもできます。通常は、テキストがあるボタンの場合、ツールチップは要りません。ボタンのラベルを見れば動作が分かるからです。

以下のカスタムコントロールを使用できます 

このビデオコンテンツの説明: アニメーション。visionOSボタンの下にツールチップが表示されます。 

再生 

visionOSでは、以下のサイズのボタンが提供されます。

形状| ミニ（28 pt）| スモール（32 pt）| レギュラー（44 pt）| ラージ（52 pt）| エクストララージ（64 pt）  
---|---|---|---|---|---  
円形| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)  
カプセル（テキストのみ）| | ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)|   
カプセル（テキストとアイコン）| | | ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)|   
角丸四角形| | ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)| ![利用できることを示すチェックマーク。](https://docs-assets.developer.apple.com/published/4978eac788e98ef1a190d030ed441aeb/table-availability-checkmark%402x.png)|   
  
**ボタンには識別可能なバックグラウンド図形と塗りつぶしを設定するのが望ましい。** 一般に、図形の中にあってバックグラウンドの塗りつぶしのコントラストが高いボタンの方が、ユーザに見えやすくなります。ただし、ツールバー、コンテキストメニュー、アラート、[オーナメント](/jp/design/human-interface-guidelines/ornaments)のボタンは例外です。それらの大きなコンポーネントの図形とマテリアルの効果で、十分にボタンを視認できるからです。さまざまな状況でボタンを確実に見えやすくするため、以下のガイドラインが役立ちます:

  * ボタンがガラス[ウインドウ](/jp/design/human-interface-guidelines/windows#visionOS)の上に表示されるときは、ボタンのバックグラウンドに[`thin`](/documentation/SwiftUI/Material/thin)マテリアルを使います。

  * ボタンが空間に浮いているように見えるときは、バックグラウンドに[ガラスマテリアル](/jp/design/human-interface-guidelines/materials#visionOS)を使います。

**白く塗りつぶされたバックグラウンドに黒いテキストまたはアイコンを表示するカスタムボタンは作成しない。** この視覚スタイルは、トグルの選択時の状態を表すものとしてシステムで指定されています。

**基本的に、円形またはカプセル型のボタンを優先して使う。** 人は図形の角に視線を引っ張られる傾向があるため、角があると項目の中央を見つめ続けるのが難しくなります。ボタンの形状に丸みがあればあるほど、ユーザはそれを注視し続けやすくなります。ボタンを単独で表示する必要がある場合は、なるべくカプセル型のボタンを使ってください。

**注視しやすいように、ボタンの周囲に十分なスペースを確保する。** ボタンの場合は、常に中心間の距離が60ポイント以上になるように配置することを心がけてください。ボタンのサイズが60ポイント以上の場合は、ホバーエフェクトが重ならないように、ボタンの周囲に4ポイントのパディングを追加します。通常、縦または横1列にスモールまたはミニサイズのボタンを並べるのは避けるのが賢明です。

**テキストラベルの付いたボタンを縦または横に並べて表示する必要がある場合は、適切な形状を選択する。** 具体的には、ボタンを縦に並べる場合は角丸四角形を、ボタンを横に並べる場合はカプセル型を優先してください。

**標準コントロールを使用してユーザに馴染みのある音声フィードバックの音を活用する。** visionOSでは触覚フィードバックが提供されないので、音声フィードバックが特に重要になります。

### [watchOS](/jp/design/human-interface-guidelines/buttons#watchOS)

watchOSでは、[`capsule`](/documentation/SwiftUI/ButtonBorderShape/capsule)のボタン形状を使ってすべてのインラインボタンが表示されます。コンテンツにインラインでボタンを配置すると、背景とのコントラストを確保するマテリアルエフェクトが得られて、可読性が確保されます。

![Apple Watchの画面の図。カプセル形状のプライマリボタンとセカンダリーボタンが含まれています。](https://docs-assets.developer.apple.com/published/5e0d976617f4a4b28bc742631e8cedc6/buttons-watch-full-width%402x.png)

**隅にボタンを配置するにはツールバーを使う。** 時刻とタイトルは、ツールバーのボタンが収まるように自動的に移動されます。また、ツールバーボタンにも[Liquid Glass](/jp/design/human-interface-guidelines/materials#Liquid-Glass)の外観が適用され、ボタンとその下にあるコンテンツがはっきりと視覚的に区別されます。

![上部の先頭側と末尾側の隅にツールバーボタンが表示されている図。画面下部にも3つのツールバーボタンが並んでいます。](https://docs-assets.developer.apple.com/published/28835a2c6f34513eb0758beef1f6015d/buttons-watch-toolbar-corners%402x.png)

**アプリのプライマリアクションを実行するボタンは、なるべく画面の幅いっぱいに表示する。** フルサイズ幅のボタンは見栄えがよく、タップもしやすくなります。2つのボタンを水平に並べなければならない場合は、両方を同じ高さにして、各ボタンのコンテンツを画像か短いテキストのタイトルにします。

**ビューのコンテンツに関連する領域やそのコンテキストアクションへのナビゲーションを提供するにはツールバーボタンを使う。** こうすることで、ビューのコンテンツの追加情報やセカンダリーアクションにアクセスできるようになります。

**1行か2行のテキストのボタンを縦に並べる場合は、同じ高さにする。** 視覚的な一貫性を保つため、できる限りボタンの高さは同じにします。

## [リソース](/jp/design/human-interface-guidelines/buttons#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/buttons#Related)

[ポップアップボタン](/jp/design/human-interface-guidelines/pop-up-buttons)

[プルダウンボタン](/jp/design/human-interface-guidelines/pull-down-buttons)

[トグル](/jp/design/human-interface-guidelines/toggles)

[セグメントコントロール](/jp/design/human-interface-guidelines/segmented-controls)

[位置情報ボタン](/jp/design/human-interface-guidelines/privacy#Location-button)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/buttons#Developer-documentation)

[`Button`](/documentation/SwiftUI/Button) — SwiftUI

[`UIButton`](/documentation/UIKit/UIButton) — UIKit

[`NSButton`](/documentation/AppKit/NSButton) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/buttons#Change-log)

日付| 変更内容  
---|---  
2025年12月16日| Liquid Glassに関するガイダンスを更新。  
2025年6月09日| ボタンのスタイルとコンテンツに関するガイダンスを更新。  
2024年2月02日| visionOSのボタンがカスタムのホバーエフェクトに対応していない点を追加。  
2023年12月05日| visionOSのボタンに関する一部の用語とガイダンスを明確化。  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2023年6月05日| watchOSでのボタンの使い方に関するガイダンスを更新。
