# 進行状況インジケータ

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/progress-indicators

# 進行状況インジケータ

進行状況インジケータは、コンテンツを読み込んだり、時間のかかる処理を実行したりしている間、アプリがフリーズしているのではないことをユーザに知らせる目的で使用します。

![図案化された進行状況バーの上で回転する不確定的なアクティビティインジケータ。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/55853c7b032cb11159791b1701541732/components-progress-indicators-intro%402x.png)

処理が完了するまでの待ち時間をユーザが推測できるインジケータもあります。進行状況インジケータは、処理が継続している間だけ表示され、処理の完了後は消去される一時的なコンポーネントです。

処理の継続時間には確定的な場合と不確定的な場合があり、それに合わせて2つのタイプの進行状況インジケータが用意されています:

  * _確定的_ : ファイル変換など継続時間が明確に定義されているタスク向け

  *  _不確定的_ : 複雑なデータの読み込みや同期など継続時間の数値化が難しいタスク向け

プログレスインジケータは、確定的、不確定的どちらの場合も、プラットフォームによって見た目が異なる場合があります。確定的なプログレスインジケータでは、タスクが完了に向かうにつれて直線また円形のバーが塗りつぶされることで、タスクの進行状況が表示されます。 _進行状況バー_ は、開始点から終了点に向かって伸びるバーです。 _円形進行状況インジケータ_ は、時計回りに伸びるバーです。

![macOSの水平進行状況バー。単色で塗りつぶされた部分がほぼ中間点にまで達しています。](https://docs-assets.developer.apple.com/published/ec2a80ba694138d5ac65555f5e3b0734/progress-indicator-determinate-bar%402x.png)進行状況バー

![macOSの円形プログレスインジケータ。単色で塗りつぶされた部分がほぼ8時の位置にまで達しています。](https://docs-assets.developer.apple.com/published/8288f9d55f529f513e7c3bd33bc3e17a/progress-indicator-determinate-circle%402x.png)円形進行状況インジケータ

不確定的進行状況インジケータは、 _アクティビティインジケータ_ とも呼ばれ、アニメーションで進行状況を示す画像が使われます。回転するように見える円形の画像は、すべてのプラットフォームに対応しています。ただし、macOSは不確定的な進行状況バーにも対応しています。

![回転するmacOSの円形アクティビティインジケータ。](https://docs-assets.developer.apple.com/published/6c1e23fcc6e04603423dacd5df6c48a3/progress-indicator-intermediate-spinner%402x.png)macOS

![回転するwatchOSのアクティビティインジケータの画像。](https://docs-assets.developer.apple.com/published/02a8427a04f946d9b80d2907f84ab365/activity-indicators-watch%402x.png)watchOS

デベロッパ向けのガイダンスは、[`ProgressView`](/documentation/SwiftUI/ProgressView)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/progress-indicators#Best-practices)

**なるべく確定的な進行状況インジケータを使う。** 不確定的なプログレスインジケーターでは、処理が進行中であることは分かりますが、当該タスクの完了までの待ち時間をユーザが推測する助けにはなりません。確定的なプログレスインジケーターは、タスクが完了するまで何かほかのことをするか、別の機会にタスクを再度実行するか、タスクを中止するかをユーザが決定する助けになります。

**確定的な進行状況インジケータの進捗度はできる限り正確に算定する。** タスクの完了までにかかる時間をできるだけ正確に予測できるように、進捗度を一定のペースで増やす方法を考えてください。90パーセントまで5秒で完了し、最後の10パーセントに5分かかるようでは、ユーザはアプリがまだ動いているのかどうか不安になりますし、ごまかされているように感じてしまうかもしれません。

**ユーザに処理が継続中であることを示すため、進行状況インジケータの動きを止めない。** インジケータが動いていないと、多くのユーザはプロセスやアプリがフリーズしていると考えます。実際に何らかの理由でプロセスがフリーズしているのであれば、ユーザが問題を理解し、対策を講じられるようなフィードバックを提示してください。

**不確定的な進行状況バーも、確定的な進行状況バーに可能な限り切り替える。** 不確定的なプロセスが、継続時間を算定できるポイントまで到達したら、確定的な進行状況バーに切り替えます。基本的に、処理内容と待ち時間を推測する助けになる確定的な進行状況インジケータの方がユーザに好まれます。

**円形スタイルとバースタイルを切り替えない。** アクティビティインジケータ（ _スピナー_ とも呼ばれます）と進行状況バーは形状もサイズも異なります。両者を切り替えて使うとインターフェイスが混乱し、ユーザが戸惑う可能性があります。

**必要に応じて、タスクの状況についての付加的な説明を表示する。** 正確さと簡潔さを心がけてください。 _「読み込んでいます」_ や _「認証しています」_ といったあいまいな表現はあまり有用ではないため避けましょう。

**プログレスインジケーターの表示位置を変えない。** 異なるプラットフォームやアプリ間、そしてアプリ内のさまざまな箇所でプログレスインジケーターを一貫して同じ場所に表示すると、処理の状況を確認しやすくなり、ユーザに安心感を与えることができます。

**可能な場合はユーザが処理を停止できるようにする。** ユーザがプロセスを中断しても悪影響が生じない場合は、キャンセルボタンを表示してください。ファイルのダウンロード済みの部分が失われるなど、プロセスの中断で悪影響が生じる可能性がある場合は、キャンセルボタンに加えて一時停止ボタンを表示することをおすすめします。

**プロセスを中止すると望ましくない結果を招く場合はユーザに知らせる。** プロセスをキャンセルすることでこれまでの進捗結果が失われる場合は、キャンセル実行を確認するか、プロセスを再開するかを選択できる[アラート](https://developer.apple.com/jp/design/human-interface-guidelines/alerts)を提示することをおすすめします。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/progress-indicators#Platform-considerations)

 _tvOS、visionOSに追加の考慮事項はありません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/progress-indicators#iOS-iPadOS)

#### [コンテンツ更新コントロール](/jp/design/human-interface-guidelines/progress-indicators#Refresh-content-controls)

更新コントロールは、一般に表形式のビューなどで、次に予定されているコンテンツの自動アップデートを待たずに直ちに再読み込みできます。更新コントロールは特殊なタイプのアクティビティインジケータで、デフォルトで非表示になっています。再読み込みしたいビューを下にドラッグすると表示されます。例えば「メール」には、受信トレイのメッセージリストを下にドラッグして新しいメッセージをチェックする機能があります。

![コンテンツ更新コントロールのスクリーンショット。「メール」で新しいメッセージをチェックしている間、回り続けます。](https://docs-assets.developer.apple.com/published/a19ce820bf000f1bdb9b24247a67254d/refresh-controls%402x.png)

**自動コンテンツアップデートを実行する。** コンテンツ更新を自分で直ちに実行できる機能はユーザにとって便利ですが、定期的に自動更新する機能も求められています。アップデート処理の開始をすべてユーザ任せにはせず、定期的にアップデートしてデータを最新の状態に保ちましょう。

**付加価値がある場合のみ短いタイトルを付ける。** 更新コントロールにはオプションでタイトルを表示できます。コントロールのアニメーションでコンテンツが読み込まれていることは分かるので、ほとんどの場合、タイトルは不要です。タイトルを表示する場合は、更新の実行方法を説明するようなタイトルではなく、更新中のコンテンツについて価値のある情報を提供するタイトルにしてください。例えば、ポッドキャストの更新コントロールでは、前回の更新日を伝えるタイトルを表示するようにしています。

デベロッパ向けのガイダンスは、[`UIRefreshControl`](/documentation/UIKit/UIRefreshControl)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/progress-indicators#macOS)

macOSでは、不確定的進行状況インジケータの見た目をバーにすることも、円形にすることもできます。どちらのバージョンも、アプリでタスクが実行中であることを示すため、アニメーション画像を使用します。

![全体が塗りつぶされたmacOSの水平進行状況バー。塗りつぶされたバーがさまざまな明るさで周期的に変化するアニメーションで、処理が継続していることを示します。](https://docs-assets.developer.apple.com/published/53c298b42043574cfe1d304c01bfc967/progress-indicator-intermediate-bar%402x.png)不確定的な進行状況バー

![回転するmacOSの円形アクティビティインジケータ。](https://docs-assets.developer.apple.com/published/6c1e23fcc6e04603423dacd5df6c48a3/progress-indicator-intermediate-spinner%402x.png)不確定な円形進行状況インジケータ

**バックグラウンド処理の状況を通知する場合やスペースに制約がある場合は、なるべくアクティビティインジケータ（スピナー）を使う。** スピナーは小さくて邪魔にならないので、サーバからメッセージを取得するような非同期のバックグラウンドタスクに適しています。スピナーは、テキストフィールドなどの小さい領域内や、ボタンなど特定のコントロールの横で進行状況を通知する場合にも役立ちます。

**回転する進行状況インジケータにはラベルを付けない。** スピナーは通常、ユーザがプロセスを開始した時に現れるので、ほとんどの場合ラベルは不要です。

### [watchOS](/jp/design/human-interface-guidelines/progress-indicators#watchOS)

デフォルトでは、シーンのバックグラウンドカラーの上に白いプログレスインジケータが表示されます。色合いを設定すると、プログレスインジケータのカラーを変えることができます。

![左から右に伸びるwatchOSの進行状況バーの画像。](https://docs-assets.developer.apple.com/published/33bbf8ea9d047a5933e60cb120d3556e/progress-bar-watch%402x.png)進行状況バー

![時計回りに伸びるwatchOSの円形の進行状況インジケータの画像。](https://docs-assets.developer.apple.com/published/9327014cf549f926741534698be7d5ee/progress-ring-watch%402x.png)円形進行状況インジケータ

![回転するwatchOSのアクティビティインジケータの画像。](https://docs-assets.developer.apple.com/published/02a8427a04f946d9b80d2907f84ab365/activity-indicators-watch%402x.png)アクティビティインジケータ

## [リソース](/jp/design/human-interface-guidelines/progress-indicators#Resources)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/progress-indicators#Developer-documentation)

[`ProgressView`](/documentation/SwiftUI/ProgressView) — SwiftUI

[`UIProgressView`](/documentation/UIKit/UIProgressView) — UIKit

[`UIActivityIndicatorView`](/documentation/UIKit/UIActivityIndicatorView) — UIKit

[`UIRefreshControl`](/documentation/UIKit/UIRefreshControl) — UIKit

[`NSProgressIndicator`](/documentation/AppKit/NSProgressIndicator) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/progress-indicators#Change-log)

日付| 変更内容  
---|---  
2023年9月12日| すべてのプラットフォームに共通するガイドを統合。  
2023年6月05日| watchOS 10の変更点を反映するためにガイダンスを更新。
