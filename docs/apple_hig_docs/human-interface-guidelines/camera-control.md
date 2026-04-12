# カメラコントロール

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/camera-control

# カメラコントロール

カメラコントロールを使用すると、アプリのカメラ体験に直接アクセスできます。

![図案化されたカメラコントロール。](https://docs-assets.developer.apple.com/published/73774a69a0e7738c02ffdaeccfe03830/inputs-camera-control-intro%402x.png)

iPhone 16およびiPhone 16 Proモデルでは、カメラコントロールでアプリのカメラ体験が素早く開き、その瞬間を捉えることができます。カメラコントロールを軽く押すと、デバイスのベゼルから延びるオーバーレイが表示されます。

![横向きのiPhoneのカメラコントロールとオーバーレイへのコールアウトのスクリーンショット。](https://docs-assets.developer.apple.com/published/783fbbd846319db1009a3fbddd2ee809/camera-control-button-callout%402x.png)

オーバーレイにより、コントロールを素早く調整できます。カメラコントロールを軽く2回押すことで、使用できるコントロールが表示されます。コントロールを選択したあと、カメラコントロールで指をスライドさせて値を調整して、コンテンツを自由に撮影することができます。

![カメラコントロールのオーバーレイのスクリーンショットの一部。そのコントロールが表示されています。](https://docs-assets.developer.apple.com/published/c44f458442bffe9bfc67341c27f291fe/camera-control-picker%402x.png)オーバーレイでのコントロール

## [構造](/jp/design/human-interface-guidelines/camera-control#Anatomy)

カメラコントロールには、値の調整とオプションの変更のための2種類のコントロールがあります:

  * _スライダ_ は、コンテンツに適用するコントラストの度合いなど、選択できる値の範囲を示します。

  *  _ピッカー_ は、ファインダー内でのグリッドのオン/オフなど、個別のオプションを示します。

![カメラコントロールのオーバーレイのスクリーンショットの一部。スライダコントロールが表示されています。](https://docs-assets.developer.apple.com/published/3bb2ecfcd292742f087c064e5dfd1ec5/camera-control-slider-control%402x.png)スライダコントロール

![カメラコントロールのオーバーレイのスクリーンショットの一部。そのピッカーコントロールが表示されています。](https://docs-assets.developer.apple.com/published/01374d652526e953dc65b175ab3b18f0/camera-control-picker-control%402x.png)ピッカーコントロール

作成するカスタムコントロールに加え、システムでは標準コントロールのセットが用意されています。これはユーザがカメラのズームや露出を調整できるようにするために、オプションとしてオーバーレイに含めることができます。

![カメラコントロールのオーバーレイのスクリーンショットの一部。システムのズーム倍率コントロールが表示されています。](https://docs-assets.developer.apple.com/published/3bb2ecfcd292742f087c064e5dfd1ec5/system-control-type-zoom-factor%402x.png)ズーム倍率コントロール

![カメラコントロールのオーバーレイのスクリーンショットの一部。システムの露出補正コントロールが表示されています。](https://docs-assets.developer.apple.com/published/47568cc559bb20a5cea03ded2199916b/system-control-type-exposure-bias%402x.png)露出補正コントロール

## [ベストプラクティス](/jp/design/human-interface-guidelines/camera-control#Best-practices)

**コントロールの機能を表すにはSF Symbolsを使用する。** システムはカスタムシンボルに対応していません。代わりに、SF Symbolsの中からコントロールの動作を明確に示すシンボルを選びます。iOSでは、アプリのオーバーレイに表示するコントロール用に何千ものシンボルが提供されています。コントロールのシンボルはコントロールの現在の状態を表すものではありません。使用可能なシンボルを確認するには、[SF Symbolsアプリ](https://developer.apple.com/sf-symbols/)の「カメラと写真」セクションを参照してください。

![カメラコントロールのオーバーレイのスクリーンショットの一部。bolt.fillシンボルを使用するカメラのフラッシュコントロールが表示されています。](https://docs-assets.developer.apple.com/published/23a133343be9226cf220b56dc0ead293/camera-control-picker-sf-symbols-flash%402x.png)カメラのフラッシュ用のコントロールを表す「bolt.fill」シンボル

![カメラコントロールのオーバーレイのスクリーンショットの一部。camera.filtersシンボルを使用するカメラのフィルタコントロールが表示されています。](https://docs-assets.developer.apple.com/published/5440b3d4c9b66e7e34e939c6a9014588/camera-control-picker-sf-symbols-filters%402x.png)フィルタ用のコントロールを表す「camera.filters」シンボル

**コントロールの名前は短くする。** コントロールのラベルはダイナミックタイプのサイズに従います。長い名前はカメラのファインダーを見えにくくすることがあります。

**状況を分かりやすくするためにスライダコントロールの値には単位や記号を付ける。** オーバーレイにEV、%、カスタム文字列などの説明情報を表示し、スライダコントロールの意味を分かりやすくします。デベロッパ向けのガイダンスは、[`localizedValueFormat`](/documentation/AVFoundation/AVCaptureSlider/localizedValueFormat)を参照してください。

![カメラコントロールのオーバーレイの例のスクリーンショットの一部。スライダコントロールに値と値の種類を表す情報が表示されています。](https://docs-assets.developer.apple.com/published/00f466e6926811164965fdb40483a34c/system-control-with-label%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)補足情報のある値

![カメラコントロールのオーバーレイの例のスクリーンショットの一部。スライダコントロールに値が表示されていますが、値の意味は表示されていません。](https://docs-assets.developer.apple.com/published/b965fe40e836dfce1361f8653c3d2abb/system-control-no-label%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)補足情報のない値

**スライダコントロールには目立つ値を定義する。** 目立つ値とは、ユーザが最も頻繁に選ぶ値や、ズーム倍率の主要な増分のような等間隔の値のことです。カメラコントロールでスライドしてスライダコントロールを調整すると、定義する目立つ値がより簡単に得られます。デベロッパ向けのガイダンスは、[`prominentValues`](/documentation/AVFoundation/AVCaptureSlider/prominentValues-199dz)を参照してください。

**ファインダー内でオーバーレイ用のスペースを作る。** オーバーレイとコントロールのラベルは、縦向きでも横向きでも、カメラコントロールに隣接している画面領域を占有します。カメラ撮影体験のインターフェイス要素に重ならないようにするには、UIをオーバーレイ領域の外側に配置します。ファインダーの高さと幅を最大にすると、オーバーレイでその上に表示したり消したりできます。

![iPhoneの縦向きと横向きのビューポート内のカメラコントロールのオーバーレイとそのコントロールのラベルのスクリーンショットの一部。](https://docs-assets.developer.apple.com/published/b55f95181bf2a40a1f4c4ee7d43aa02c/camera-control-portrait-landscape-orientation%402x.png)

**ファインダー内では気を散らすものの表示をできるだけ減らす。** 写真やビデオを撮影する際は、視覚的に余計なものをなくした大きなプレビュー画像がユーザに喜ばれます。システムでオーバーレイが表示される場合は、スライダやトグルなどのコントロールがUIとオーバーレイで重複しないようにします。

![カメラコントロールのオーバーレイの例のスクリーンショットの一部。UI要素が撮影ビューポートから削除されています。](https://docs-assets.developer.apple.com/published/9cd4da3793671dd837c50d855ab265df/camera-control-screen-ui-good-example%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)UIは最小限に抑えます。

![カメラコントロールのオーバーレイの例のスクリーンショットの一部。UI要素が撮影ビューポートで重複しています。](https://docs-assets.developer.apple.com/published/eb4a1bc88b0f16c3074d57f8ff3afb9f/camera-control-screen-ui-bad-example%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)オーバーレイでユーザがアクセスするコントロールをファインダーに表示しないようにします。

**コントロールはカメラモードに応じて有効/無効にする。** 例えば、写真を撮るときはビデオコントロールを無効にします。オーバーレイは複数のコントロールに対応していますが、実行時にコントロールを追加したり削除したりすることはできません。

**コントロールの配置方法を検討する。** 素早くアクセスできるようによく使うコントロールを中央の方に配置し、あまり使わないコントロールを左端や右端の方に配置します。カメラコントロールを軽く押してオーバーレイをもう一度開くと、アプリで最後に使用されたコントロールが記憶されます。

**ユーザがカメラコントロールを使用して、どこからでも体験を開始できるようにする。** ユーザがカメラコントロールを構成して、ロックされたデバイスやホーム画面、またはほかのアプリ内からアプリのカメラ体験を開始できるように、ロックされたカメラ撮影の機能拡張を作成します。ガイダンスは[ロックされたデバイスでのカメラ体験](/jp/design/human-interface-guidelines/controls#Camera-experiences-on-a-locked-device)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/camera-control#Platform-considerations)

 _iPadOS、macOS、watchOS、tvOS、visionOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/camera-control#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/camera-control#Related)

[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)

[コントロール](/jp/design/human-interface-guidelines/controls)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/camera-control#Developer-documentation)

[カメラコントロールでアプリ体験を強化する](/documentation/AVFoundation/enhancing-your-app-experience-with-the-camera-control) — AVFoundation

[`AVCaptureControl`](/documentation/AVFoundation/AVCaptureControl) — AVFoundation

[LockedCameraCapture](/documentation/LockedCameraCapture)

## [変更履歴](/jp/design/human-interface-guidelines/camera-control#Change-log)

日付| 変更内容  
---|---  
2024年9月09日| 新規ページ。
