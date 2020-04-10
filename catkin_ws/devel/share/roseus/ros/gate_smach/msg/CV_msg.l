;; Auto-generated. Do not edit!


(when (boundp 'gate_smach::CV_msg)
  (if (not (find-package "GATE_SMACH"))
    (make-package "GATE_SMACH"))
  (shadow 'CV_msg (find-package "GATE_SMACH")))
(unless (find-package "GATE_SMACH::CV_MSG")
  (make-package "GATE_SMACH::CV_MSG"))

(in-package "ROS")
;;//! \htmlinclude CV_msg.msg.html


(defclass gate_smach::CV_msg
  :super ros::object
  :slots (_name _center ))

(defmethod gate_smach::CV_msg
  (:init
   (&key
    ((:name __name) "")
    ((:center __center) nil)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _center __center)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:center
   (&optional __center)
   (if __center (setq _center __center)) _center)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; bool _center
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; bool _center
       (if _center (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _center
     (setq _center (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get gate_smach::CV_msg :md5sum-) "f97c3665b94139c47928a4e2b9761f46")
(setf (get gate_smach::CV_msg :datatype-) "gate_smach/CV_msg")
(setf (get gate_smach::CV_msg :definition-)
      "string name
bool center
")



(provide :gate_smach/CV_msg "f97c3665b94139c47928a4e2b9761f46")


