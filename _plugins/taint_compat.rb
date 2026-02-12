# Compatibility shim: Ruby 3.2 removed Kernel/Object taint APIs
# Liquid (and other gems) may call `obj.tainted?`; define a safe no-op
# implementation so builds on Ruby >= 3.2 don't blow up.
unless Object.method_defined?(:tainted?)
  class Object
    def tainted?
      false
    end
  end
end
