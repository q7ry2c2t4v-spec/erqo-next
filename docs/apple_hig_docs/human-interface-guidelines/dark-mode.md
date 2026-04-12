# ダークモード

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/dark-mode

# ダークモード

ダークモードはシステム全体の外観設定で、暗いカラーパレットを使用して低照度環境で快適な表示体験を実現します。

![半分ずつ塗りつぶされた同心円のスケッチ。ライトとダークの存在を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる黄色になっています](https://docs-assets.developer.apple.com/published/16d52d078659c3b1cfaf84687e911060/foundations-dark-mode-intro%402x.png)

iOS、iPadOS、macOS、tvOSでは、多くのユーザがデフォルトのインターフェイススタイルをダークモードにしており、ユーザはその環境設定がすべてのアプリやゲームに反映されることを期待します。ダークモードでは、すべての画面、ビュー、メニュー、コントロールで暗いカラーパレットが使われます。また、暗い背景に対してフォアグラウンドにあるコンテンツが引き立つように、知覚のコントラストを大きくすることもできます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/dark-mode#Best-practices)

**アプリ固有の外観設定を作らない。** アプリ固有の外観モードオプションを作ると、望む見た目を実現するために複数の設定を調整しなければいけなくなるので、ユーザの作業を増やすことになります。さらに悪いことに、システム全体の外観設定に反応しないため、アプリが正しく動作していないと思われる可能性もあります。

**両方の外観モードでアプリが見やすいことを確認する。** ユーザは、片方のモードだけを使用するのではなく、「自動」設定を使用して、1日の条件変化に応じてライトとダークを切り替える可能性があります。切り替えがアプリの動作中に起こる可能性もあります。

**両方のモードでコンテンツが快適に読めるかをテストする。** 例えば、ダークモードで「コントラストを上げる」や「透明度を下げる」がオンになっている場合（どちらかの場合も両方の場合も含む）、暗い背景にある暗いカラーのテキストが読みにくくなる場所ができる可能性があります。また、ダークモードで「コントラストを上げる」をオンにすると、暗いテキストと暗い背景との間でのコントラストが下がる可能性があります。視力が良好なユーザは、テキストのコントラストが低くても読めるかもしれませんが、そのようなテキストを読めないユーザも多く存在するかもしれません。ガイダンスは[アクセシビリティ](/jp/design/human-interface-guidelines/accessibility)を参照してください。

**場合によってはインターフェイスにダークな外観のみを使用することを検討する。** 例えば、イマーシブ感のあるメディア視聴アプリでは、UIを目立たせずにメディアに集中できるようにするため、常にダークな外観を使用した方がよいかもしれません。

![iPhoneの株価アプリのスクリーンショット。標準のダークな外観のみで、Apple Inc.の詳しい株価が表示されています。ビューには、現在の株価の概要と過去1年間の実績のグラフが含まれています。](https://docs-assets.developer.apple.com/published/dd3141ef638f2a2726b6044c93459178/dark-mode-stocks-app-dark-only-mode%402x.png)

株価アプリでダークな外観のみが使用されています

## [ダークモードのカラー](/jp/design/human-interface-guidelines/dark-mode#Dark-Mode-colors)

ダークモードのカラーパレットは、薄暗いバックグラウンドカラーと明るいフォアグラウンドカラーで構成されています。これらのカラーが、必ずしもライトモードでの対応カラーの反対色ではない点を認識しておくことが重要です。ほとんどのカラーは反対色ですが、例外もあります。詳しくは、[仕様](/jp/design/human-interface-guidelines/color#Specifications)を参照してください。

**現在の外観に適応したカラーを使用する。** セマンティックカラー（macOSの[`labelColor`](/documentation/AppKit/NSColor/labelColor)や[`controlColor`](/documentation/AppKit/NSColor/controlColor)、iOSとiPadOSの[`separator`](/documentation/UIKit/UIColor/separator)など）は、自動的に現在の外観に適応します。カスタムカラーが必要な場合は、XcodeでアプリのアセットカタログにColor Setアセットを追加し、そのカラーの明るいバリエーションと暗いバリエーションを指定します。カラーの値をハードコードしたり、適応しないカラーを使用したりしないでください。

![明るい背景の正方形と、ライトな外観でのシステムカラーを表す4つのカラー見本の図。](https://docs-assets.developer.apple.com/published/083d8f0f70c26b7fdea230f7da1edfeb/dark-mode-system-colors-light%402x.png)ライトな外観でのシステムカラー

![暗い背景の正方形と、ダークな外観でのシステムカラーを表す4つのカラー見本の図。](https://docs-assets.developer.apple.com/published/247df4f7b00e65cdd3827de84135fcda/dark-mode-system-colors-dark%402x.png)ダークな外観でのシステムカラー

**すべての外観で十分な色のコントラストを確保する。** システムで定義されたカラーを使うことで、フォアグラウンドとバックグラウンドのコンテンツ間の十分なコントラスト比を実現できます。最低でも、カラー間のコントラスト比が4.5:1を下回らないようにしてください。カスタムのフォアグラウンドカラーとバックグラウンドカラーを使用する場合は、コントラスト比7:1を目指すようにします。テキストが小さい場合は、特にこの点に注意してください。この比率を確保すると、背景に対してフォアグラウンドにあるコンテンツが目立つようになるだけでなく、推奨されるアクセシビリティガイドラインを満たすコンテンツを実現する上でも役立ちます。

**白い背景の色をやわらげる。** 白い背景を含むコンテンツ画像を表示する場合は、ダークモードで背景が光りすぎないように、わずかに画像を暗くすることを検討します。

### [アイコンと画像](/jp/design/human-interface-guidelines/dark-mode#Icons-and-images)

システムは、[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)（自動的にダークモードに対応します）と、ライトとダークの両方の外観に最適化されたフルカラー画像を使用します。

**可能な限りSF Symbolsを使用する。** ダイナミックカラーを使用して色を合わせたり、バイブランスを追加したりしても、シンボルは両方の外観モードで適切に表示されます。ガイダンスは、[カラー](/jp/design/human-interface-guidelines/color)を参照してください。

**必要な場合は、ライトとダークの外観で別のインターフェイスアイコンをデザインする。** 例えば、満月を表すアイコンには、明るい背景でもはっきりと見えるように、わずかに暗い輪郭が必要かもしれませんが、暗い背景に表示する場合は輪郭は必要ありません。同じように、油のしずくを表すアイコンには、暗い背景でも見えるように、細い縁取りが必要かもしれません。

![黒いしずくのアイコンの図。明るい背景の上に配置されています。](https://docs-assets.developer.apple.com/published/5377a16f9c47c32d5716a2de9e7e5ddb/dark-mode-icon-in-light-mode%402x.png)ライトな外観で縁取りのないアイコン

![黒いしずくのアイコンの図。暗い背景の上に配置されています。アイコンには白い枠線があり、似たような周囲のカラーと区別できるようになっています。](https://docs-assets.developer.apple.com/published/a2ebe256a3e677367cc3e965e8282168/dark-mode-icon-in-dark-mode%402x.png)ダークな外観で識別しやすい縁取りのあるアイコン

**両方の外観でフルカラーの画像やアイコンが適切に表示されるようにする。** ライトとダークの両方の外観で適切に表示される場合は、同じアセットを使用します。片方のモードでしか適切に表示されない場合は、アセットを変更するか、ライトとダークで別のアセットを作成します。アセットカタログを使用すると、複数のアセットを組み合わせて1つの名前付き画像にすることができます。

![レストランのテーブル席に座っている2人の客の図。シンプルで抽象的なスタイルで描かれています。図の背景は明るく、細かいところまではっきりと見えます。](https://docs-assets.developer.apple.com/published/017a90f0e42a841edec3d4238f408e9e/dark-mode-illustration-in-light-mode%402x.png)明るい背景の上にある図

![レストランのテーブル席に座っている2人の客の図。シンプルで抽象的なスタイルで描かれています。図の背景は暗く、画像の暗い部分が背景と見分けにくくなっています。](https://docs-assets.developer.apple.com/published/97c07bc517069bf9175e7a3374ed95aa/dark-mode-illustration-in-dark-mode-incorrect%402x.png)暗い背景では同じ図が識別しにくくなり、多くの細部が見えなくなっています

![レストランのテーブル席に座っている2人の客の図。シンプルで抽象的なスタイルで描かれています。図の背景は暗く、背景に対してはっきりと見えるようにカラー値が調整されています。](https://docs-assets.developer.apple.com/published/fa4aec31ae33aadce2ed0a0434c9c605/dark-mode-illustration-in-dark-mode-correct%402x.png)暗い背景で見やすくなるように調整された図

### [テキスト](/jp/design/human-interface-guidelines/dark-mode#Text)

システムは、バイブランスと高いコントラスト比を使用して、暗い背景でもテキストがはっきりと読めるようにします。

**ラベルにはシステムが提供するラベルカラーを使用する。** 第1、第2、第3、第4のラベルカラーは、ライトとダークの外観に自動的に適応します。

![ライトな外観のボタンの図。テキストはダークの第1ラベルです。](https://docs-assets.developer.apple.com/published/b5ea9a0f4083fadf9ec4220a423edb64/dark-mode-label-in-light-mode%402x.png)ライトな外観での第1ラベル

![ダークな外観のボタンの図。テキストはライトの第2ラベルです。](https://docs-assets.developer.apple.com/published/aade73b422282dea3d64ed4d01c9615d/dark-mode-label-in-dark-mode%402x.png)ダークな外観での第2ラベル

**システムのビューを使用してテキストフィールドやテキストビューを描画する。** システムのビューやコントロールは、バイブランスの有無に応じて自動的に調整を行い、あらゆる背景でアプリのテキストを適切に表示します。テキストは独自の方法で表示するのではなく、できるだけシステムが提供するビューを使用して表示してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/dark-mode#Platform-considerations)

 _tvOSに追加の考慮事項はありません。ダークモードはvisionOSとwatchOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/dark-mode#iOS-iPadOS)

ダークモードでは、 _ベース_ と _高階調_ という2つのバックグラウンドカラーのセットが使用されます。これにより、一方のダークなインターフェイスをもう一方のインターフェイスに重ねたときに、奥行き感を表現することができます。ベースカラーの方が色が暗く、バックグラウンドインターフェイスが後退して見えます。高階調カラーの方が明るく、フォアグラウンドインターフェイスが前に出て見えます。

![黒の背景の上に縦に並んだ4つの語句が表示されています。一番上の語句は背景に対するコントラストが最も強く、一番下の語句は最も弱くなっています。](https://docs-assets.developer.apple.com/published/6855fabb5ab5b226c96756af2f898eac/base-with-four-semantic-colors%402x.png)ベース

![ほぼ黒の背景の上に縦に並んだ4つの語句が表示されています。一番上の語句は背景に対するコントラストが最も強く、一番下の語句は最も弱くなっています。](https://docs-assets.developer.apple.com/published/24108d80251edb00ba1fc3436606e8e0/elevated-with-four-semantic-colors%402x.png)高階調

![白の背景の上に縦に並んだ4つの語句が表示されています。一番上の語句は背景に対するコントラストが最も強く、一番下の語句は最も弱くなっています。](https://docs-assets.developer.apple.com/published/90ba885282182cf85656b15a73bd1334/light-with-four-semantic-colors%402x.png)ライト

**システムのバックグラウンドカラーを優先する。** ダークモードはダイナミックです。つまり、ポップオーバーやモーダルシートなどのようにインターフェイスがフォアグラウンドにある場合には、バックグラウンドカラーがベースから高階調に自動的に変化します。また、マルチタスク環境のアプリを視覚的に区別したり、複数ウインドウ環境でウインドウを区別したりする場合にも、高階調のバックグラウンドカラーが使用されます。カスタムのバックグラウンドカラーを使用すると、システムが提供する視覚的な区別を認識しにくくなる場合があります。

### [macOS](/jp/design/human-interface-guidelines/dark-mode#macOS)

ユーザが「一般」設定のアクセントカラーでグラファイトを選択すると、macOSは現在のデスクトップピクチャの色からウインドウの背景を選択します。この処理は _デスクトップの色合い調整_ と呼ばれますが、これにより、ウインドウが周囲のコンテンツとなじむようにブレンドされるわずかな効果が追加されます。

**適切な場合は、カスタムコンポーネントの背景に多少の透明度を加える。** 透明度を加えると、デスクトップの色合い調整が行われる場合にコンポーネントにウインドウのバックグラウンドカラーが混ざるので、デスクトップピクチャが変わった場合でも、常に視覚的な調和が維持されるようになります。この調和を実現するには、目に見える背景やベゼルがあるカスタムコンポーネントが自然な状態（カラーを使わない状態など）にある場合にのみ、透明度を追加します。コンポーネントがカラーを使う状態にあるときは、透明度を追加する必要はありません。追加すると、デスクトップの別の場所でウインドウの背景が調整されたときや、デスクトップピクチャが変わったときに、コンポーネントのカラーが変化する可能性があります。

## [リソース](/jp/design/human-interface-guidelines/dark-mode#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/dark-mode#Related)

[カラー](/jp/design/human-interface-guidelines/color)

[マテリアル](/jp/design/human-interface-guidelines/materials)

[タイポグラフィ](/jp/design/human-interface-guidelines/typography)

#### [ビデオ](/jp/design/human-interface-guidelines/dark-mode#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/219)

[](https://developer.apple.com/videos/play/wwdc2019/214)

## [変更履歴](/jp/design/human-interface-guidelines/dark-mode#Change-log)

日付| 変更内容  
---|---  
2024年8月06日| ライトとダークの外観の違いを示した画像を追加。
