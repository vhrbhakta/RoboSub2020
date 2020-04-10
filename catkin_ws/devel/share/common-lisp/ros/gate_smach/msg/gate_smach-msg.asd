
(cl:in-package :asdf)

(defsystem "gate_smach-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CV_msg" :depends-on ("_package_CV_msg"))
    (:file "_package_CV_msg" :depends-on ("_package"))
  ))