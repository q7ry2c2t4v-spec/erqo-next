# VoiceOver

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/voiceover

# VoiceOver

VoiceOverは画面読み上げ機能です。VoiceOverを使うと、画面を見ずにアプリのインターフェイスを使うことができます。

![VoiceOverアイコンのスケッチ。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/477ffccb67999218b412ec3b1466e58d/technologies-VoiceOver-intro%402x.png)

VoiceOverに対応すると、目の不自由な方や弱視の方がアプリの情報にアクセスしたり、画面が見えないときにインターフェイスやコンテンツを操作したりできるようになります。

VoiceOverは、Appleプラットフォーム向けに作成されたアプリやゲームに対応しています。[AppleのUnityプラグイン](https://github.com/apple/unityplugins)を使用してUnityで開発したアプリやゲームにも対応しています。関連するガイダンスは[アクセシビリティ](/jp/design/human-interface-guidelines/accessibility)を参照してください。

## [説明](/jp/design/human-interface-guidelines/voiceover#Descriptions)

アプリに表示されるインターフェイスやコンテンツについて説明する別のテキストを提供すると、VoiceOverにアプリのコンテンツについての情報を提示できます。

**すべての重要なインターフェイス要素に代替ラベルを付ける。** VoiceOverは、別のラベル（画面には表示されません）を使用してアプリのインターフェイスを音声で説明します。システムが提供するコントロールには一般的なラベルがデフォルトで付いていますが、アプリの機能を詳しく説明するラベルを付けるようにしてください。アプリで定義したすべてのカスタム要素にラベルを追加します。アプリのインターフェイスやコンテンツの変化に合わせて説明を更新する必要があります。デベロッパ向けのガイダンスは、[アクセシビリティモディファイア](/documentation/SwiftUI/View-Accessibility)を参照してください。

**意味のある画像を説明する。** アプリのコンテンツに含まれる重要な画像を説明しなければ、VoiceOverでアプリのすべてを体験することはできません。ユーザはVoiceOverによって近くのキャプションなどの画像の周囲のインターフェイスも理解できるので、画像自体が伝える情報のみを説明してください。

**グラフなどのインフォグラフィックはアクセシビリティに完全対応させる。** すべてのインフォグラフィックに、それが伝えている内容の簡潔な説明を付けます。インフォグラフィックを操作するとさらに詳しい情報や別の情報を得られる場合は、VoiceOverでもこれらの操作を実行できるようします。アクセシビリティAPIを使えば、ユーザが操作補助技術を介して操作できる、インタラクティブなカスタム要素を提示することができます。ガイダンスは[グラフ](/design/Human-Interface-Guidelines/charts#Enhancing-the-accessibility-of-a-chart)を参照してください。

**純粋な装飾用途の画像はVoiceOverから除外する。** 有用な情報や実用的な情報を伝えない装飾の画像を説明する必要はありません。このような画像を除外することで、VoiceOverを使うユーザの時間を無駄にせず、認知負荷を減らすことができます。デベロッパ向けのガイダンスは、[`accessibilityHidden(_:)`](/documentation/SwiftUI/View/accessibilityHidden\(_:\))、[`accessibilityElement`](/documentation/AppKit/NSAccessibility-c.protocol/accessibilityElement)および[`isAccessibilityElement`](/documentation/UIKit/UIAccessibilityElement/isAccessibilityElement)を参照してください。

## [ナビゲーション](/jp/design/human-interface-guidelines/voiceover#Navigation)

**タイトルや見出しを使って情報階層を移動できるようにする。** ユーザがアプリのページや画面を開いたとき、操作補助技術から得られる最初の情報がタイトルです。固有のタイトルを提示し、各ページの内容や目的を簡潔に説明するようにします。同様に、各ページの情報階層をイメージしやすいように、セクションに正確な見出しを付けるようにしてください。

**要素のグループ化、順序付け、リンクを設定する。** 視覚に障がいのないユーザは、要素間の間隔や位置によって要素の関係を容易に把握できます。要素間の関係が視覚のみで提示されている箇所がないかアプリを検査してください。そうした箇所があれば、その関係性の説明をVoiceOverに提供してください。

VoiceOverは、現在の言語や地域でコンテンツを読む順序に合わせて要素を読み上げます。例えば、米国の英語では上から下、左から右になります。下のグループ化されていない例では、VoiceOverはキャプションに移る前に各画像を説明します。グループ化されている例では、VoiceOverはそれぞれのキャプションと合わせて各画像を説明します。

![iPhoneの上部の図。画面のUIに2つの画像が表示されています。左側はマンゴーが入ったバスケット、右側はアーティチョークが入ったバスケットです。画像の下にキャプションがあり、「マンゴーはマンゴー属の木から採れます」、「アーティチョークはアザミの一種から育てられます」と書かれています。画像とキャプションは、すべて1つのVoiceOverフレームに含まれています。](https://docs-assets.developer.apple.com/published/164a6323c5f3d7ec48c750a90eddd4ad/voiceover-incorrect-grouping%402x.png)

関連要素がグループ化されていないと、VoiceOverがUIを正確に説明するのは難しくなります。

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![iPhoneの上部の図。画面のUIに2つの画像が表示されています。左側はマンゴーが入ったバスケット、右側はアーティチョークが入ったバスケットです。画像の下にキャプションがあり、「マンゴーはマンゴー属の木から採れます」、「アーティチョークはアザミの一種から育てられます」と書かれています。マンゴーの画像とキャプションだけが1つのVoiceOverフレームに含まれています。](https://docs-assets.developer.apple.com/published/0965e3a106c0727f2b62404a1874f9e7/voiceover-correct-grouping%402x.png)

関連要素がグループ化されていると、VoiceOverはUIを正確に説明できます。

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

デベロッパ向けのガイダンスは、[`shouldGroupAccessibilityChildren`](/documentation/ObjectiveC/NSObject-swift.class/shouldGroupAccessibilityChildren)を参照してください。

**コンテンツやレイアウトの見た目が変化したらVoiceOverに通知する。** コンテンツやレイアウトが予期せず変化すると、ユーザが頭に描いているコンテンツのイメージと合わなくなるため、混乱のもとになりかねません。VoiceOverなどの操作補助技術によって、ユーザが最新の画面状態を把握できるように、見た目の変化をVoiceOverに通知することはきわめて重要です。デベロッパ向けのガイダンスは、[`AccessibilityNotification`](/documentation/Accessibility/AccessibilityNotification)を参照してください。

**可能な場合はVoiceOverローターに対応する。** ユーザは、VoiceOverローターと呼ばれるインターフェイス要素を使って、見出しやリンクなどのコンテンツタイプごとに書類やWebページ内を移動できます。これらの要素をローターに認識させることで、ユーザがアプリ内のコンテンツを移動しやすくなります。ローターで点字キーボードも表示できます。デベロッパ向けのガイダンスは、[`AccessibilityRotorEntry`](/documentation/SwiftUI/AccessibilityRotorEntry)（SwiftUI）、[`UIAccessibilityCustomRotor`](/documentation/UIKit/UIAccessibilityCustomRotor)（UIKit）、および[`NSAccessibilityCustomRotor`](/documentation/AppKit/NSAccessibilityCustomRotor)（AppKit）を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/voiceover#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、watchOSに追加の考慮事項はありません。_

### [visionOS](/jp/design/human-interface-guidelines/voiceover#visionOS)

**カスタムジェスチャが常に利用できるとは限らないことを意識する。** visionOSでVoiceOverがオンになっているとき、カスタムジェスチャが定義されているアプリやゲームは、デフォルトでは手入力を受け取りません。これは、アプリが同時に手入力に応答することなく、声でインターフェイスを操作できるようにするためです。この動作を無効にするには、直接的ジェスチャモードを有効にします。すると標準のVoiceOverジェスチャが無効になり、アプリが手入力を直接処理できるようになります。デベロッパ向けのガイダンスは、[visionOSアプリでのアクセシビリティ対応を改善する](/documentation/visionOS/improving-accessibility-support-in-your-app)を参照してください。

## [リソース](/jp/design/human-interface-guidelines/voiceover#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/voiceover#Related)

[アクセシビリティ](/jp/design/human-interface-guidelines/accessibility)

[インクルージョン](/jp/design/human-interface-guidelines/inclusion)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/voiceover#Developer-documentation)

[Accessibility](/documentation/Accessibility)

[VoiceOver](/documentation/Accessibility/voiceover)

[アプリをVoiceOverに対応させる](/documentation/UIKit/supporting-voiceover-in-your-app)

#### [ビデオ](/jp/design/human-interface-guidelines/voiceover#Videos)

[](https://developer.apple.com/videos/play/wwdc2019/254)

[](https://developer.apple.com/videos/play/wwdc2021/10121)

[](https://developer.apple.com/videos/play/wwdc2020/10116)

## [変更履歴](/jp/design/human-interface-guidelines/voiceover#Change-log)

日付| 変更内容  
---|---  
2025年3月07日| 新規ページ。
